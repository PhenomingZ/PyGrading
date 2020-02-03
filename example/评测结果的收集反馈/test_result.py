import pygrading.general_test as gg


def prework(job):
    testcases = gg.create_testcase(100)

    for i in range(1, 5):
        input_src = i
        output_src = pow(2, i)
        testcases.append("TestCase{}".format(i), 25, input_src, output_src)

    job.set_testcases(testcases)


def run(job, testcase):
    # 使用Shell命令计算2^n
    cmd = ["echo", "$((", "2", "**", str(testcase.input_src), "))"]

    # 获取执行情况
    status, output, time = gg.utils.bash(" ".join(cmd))

    # 初始化返回结果的字典
    result = {"name": testcase.name, "time": time}

    # 获取评测用例给出的答案
    answer = testcase.output_src

    result["output"] = output
    result["answer"] = answer

    # 根据字符串比较结果返回单个测试用例的评判情况
    if gg.utils.compare_str(str(output), str(answer)):
        result["verdict"] = "Accept"
        result["score"] = testcase.score
    else:
        result["verdict"] = "Wrong Answer"
        result["score"] = 0

    return result


def postwork(job):
    # 打印收集到的每个评测用例的结果
    print(job.get_summary())


myjob = gg.job(prework=prework, run=run, postwork=postwork)

myjob.start()
