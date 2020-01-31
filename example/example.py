import pygrading.general_test as gg
from pygrading.html import *


def prework(job):
    config = gg.load_config("./example/config.json")
    testcases = gg.create_std_testcase(config["testcase_dir"], config["testcase_num"])

    job.set_config(config)
    job.set_testcases(testcases)


def run(job, testcase):
    configuration = job.get_config()

    cmd = ["cat", testcase.input_src, "|", "python3 " + configuration["submit_path"]]
    status, output, time = gg.utils.bash(" ".join(cmd))

    result = {"name": testcase.name, "time": time}

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
    ver = font(color="green").set_text("Accept")
    job.verdict(str(ver))
    job.score(job.get_total_score())
    job.rank({"rank": str(job.get_total_time())})
    detail = table(
        tr(
            th(),
            th().set_text("Verdict"),
            th().set_text("Output"),
            th().set_text("Answer")
        ), border="1"
    )
    for i in job.get_summary():
        if i["verdict"] == "Runtime Error":
            ver = font(color="red").set_text("Runtime Error")
            job.verdict(str(ver))
        elif i["verdict"] == "Wrong Answer":
            ver = font(color="red").set_text("Wrong Answer")
            job.verdict(str(ver))

        row = tr(
            td().set_text(str2html(i["name"])),
            td(align="center").set_text(str2html(i["verdict"])),
            td(align="center").set_text(str2html(i["output"])),
            td(align="center").set_text(str2html(i["answer"]))
        )
        detail << row
    detail = str(detail)
    job.detail(detail)


new_job = gg.job(prework=prework, run=run, postwork=postwork)

new_job.start()

new_job.print()
