import pygrading.general_test as gg


def prework(job):
    config = gg.load_config("./example/构建并读取评测用例/config_std.json")
    testcases = gg.create_std_testcase(config["testcase_dir"], config["testcase_num"])

    job.set_testcases(testcases)


def run(job, testcase):
    print("######################")
    print(testcase.name)
    print(testcase.score)
    print(testcase.input_src)
    print(testcase.output_src)
    print(testcase.extension)


myjob = gg.job(prework=prework, run=run, postwork=None)

myjob.start()
