import pygrading.general_test as gg


def prework(job):
    config = gg.load_config("./example/config.json")
    testcases = gg.create_std_testcase(config["testcase_dir"], config["testcase_num"])

    job.set_config(config)
    job.set_testcases(testcases)

    compile_result = gg.compiler.compile_c(config["submit_path"], config["exec_path"])

    if compile_result[0]:
        job.verdict("Compile Error")
        job.score(0)
        job.detail(compile_result[1].replace("\n", "<br>"))
        job.terminate()


def run(job, testcase):
    configuration = job.get_config()

    cmd = ["cat", testcase.input_src, "|", configuration["exec_path"]]
    status, output, time = gg.utils.bash(" ".join(cmd))

    result = {"name": testcase.name, "time": time}

    if status:
        result["verdict"] = "Runtime Error"
        result["score"] = 0
        result["log"] = output
        return result

    answer = gg.utils.readfile(testcase.output_src)

    result["output"] = output
    result["answer"] = answer
    if gg.utils.compare_str(output, answer):
        result["verdict"] = "Accept"
        result["score"] = testcase.score
    else:
        result["verdict"] = "Wrong Answer"
        result["score"] = 0

    return result


def postwork(job):
    job.verdict("Accept")
    job.score(job.get_total_score())
    job.rank({"rank": str(job.get_total_time())})
    detail = {}
    for i in job.get_summary():
        if i["verdict"] == "Runtime Error":
            job.verdict("Runtime Error")
        elif i["verdict"] == "Wrong Answer":
            job.verdict("wrong Answer")
            detail[i["name"]] = {
                "output": i["output"],
                "answer": i["answer"]
            }
    job.detail(detail)


new_job = gg.job(prework=prework, run=run, postwork=postwork)

new_job.start()

new_job.print()
