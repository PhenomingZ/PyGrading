import pygrading.general_test as gg

a = gg.create_testcase(50)

a.append(
    name="TestCase",
    score=10,
    input_src="input_scr",
    output_src="output_src"
)

print(a)