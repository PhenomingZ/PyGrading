import pygrading.general_test as gg

config = gg.load_config("./example/config.json")

testcases = gg.get_std_testcase(config["testcase_dir"], config["testcase_num"])

print(gg.compiler.compile_c(config["submit_path"], config["exec_path"]))
