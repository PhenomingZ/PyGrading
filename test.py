import pygrading.general_test as gg

config = gg.load_config("./example/config.json")

testcases = gg.get_std_testcase(config["testcase_dir"], config["testcase_num"])

compile_result = gg.compiler.compile_c(config["submit_path"], config["exec_path"])

if compile_result[0]:
    # TODO 添加输出内容处理模块
    pass

print(compile_result)
