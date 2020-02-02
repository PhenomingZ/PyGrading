import pygrading.general_test as gg


def prework(job):
    config = gg.load_config("./example/构建并读取配置文件/config.json")
    job.set_config(config)


def postwork(job):
    config = job.get_config()
    testcase_num = config["testcase_num"]
    testcase_dir = config["testcase_dir"]
    submit_path = config["submit_path"]

    print("testcase_num:", testcase_num)
    print("testcase_dir:", testcase_dir)
    print("submit_path:", submit_path)


myjob = gg.job(prework=prework, run=None, postwork=postwork)

myjob.start()
