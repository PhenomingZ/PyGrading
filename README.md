<h1 align="center">PyGrading</h1>

<p align="center">CourseGrading(希冀)计算机专业课一体化在线平台开发用Python工具包。包含通用评测内核创建以及HTML标签生成工具。</p>

<p align="center">
	<a href="http://www.educg.net/">
		<img src="https://img.shields.io/badge/site-CG-red"
				 alt="Official Site">
	</a>
	<a href="https://github.com/PhenomingZ/PyGrading">
		<img src="https://img.shields.io/github/stars/PhenomingZ/PyGrading"
				 alt="GitHub stars">
	</a>
	<a href="https://pypi.org/project/pygrading/">
			<img src="https://img.shields.io/badge/pypi-v0.2.0-orange"
					 alt="Pypi package">
		</a>
	<a href="https://github.com/PhenomingZ/PyGrading/issues">
				<img src="https://img.shields.io/github/issues/PhenomingZ/PyGrading"
						 alt="GitHub issues">
	</a>
	<a href="https://github.com/PhenomingZ/PyGrading/blob/master/LICENSE">
				<img src="https://img.shields.io/github/license/PhenomingZ/PyGrading"
						 alt="GitHub license">
	</a>
</p>

<p align="center">
	<a href="#what-is-it">What is it</a> •
	<a href="#install">Install</a> •
	<a href="#getting-start">Getting Start</a> •
	<a href="http://www.educg.net/" target="_blank">Site</a>
</p>

<p align="center">
		<img src="./img/logo.png" width="200">
</p>

<h6 align="center">Made by Charles Zhang • :globe_with_meridians: <a href="https://github.com/PhenomingZ">https://github.com/PhenomingZ</a></h6>

<h2 id="what-is-it" align="center">What is it</h2>

**希冀平台** 是一个国内最具专业深度、安全可扩展的计算机类课程一体化支撑平台，是一个定位于全面支撑计算机、人工智能和大数据专业建设的大型综合教学实验平台，而非一个只能支撑若干门课程的实验系统。

**通用评测** 是一个通用的自动评测框架，基于该框架可以定制开发任何自己需要的自动评测内核。

**PyGrading工具包** 目前该工具包包含以下功能：
1. 支持CourseGrading平台通用评测内核快速构建；
2. 支持适用于通用评测题和虚拟桌面环境的评测结果JSON串的快速生成；
2. 支持HTML标签文本内容的快速生成，绝对好用的HTML生成工具；

希望使用本工具能够提高大家的工作效率，祝各位开发顺利！

<h2 id="install" align="center">Install</h2>

使用pip可以轻松安装PyGrading：

```bash
pip install pygrading
```

也可以下载项目文件后，切换到`setup.py`所在的目录，执行以下命令来安装：

```bash
python setup.py install
```

PyGrading的运行环境要求 **Python >= 3.6**，不支持Python2。

<h2 id="getting-start" align="center">Getting Start</h2>

### 通用评测内核构建

#### 1. 设计逻辑

PyGrading采用三段式的设计逻辑，将每一次评测任务分为三个阶段，分别完成“评测任务预处理”、“评测用例执行”、“评测结果处理”，如下图所示：

<p align="center">
		<img src="./img/flow.png" width="500">
</p>

**评测任务预处理** 通常包括读取配置文件信息、读取评测用例信息、编译学生提交的文件等任务。

**评测用例执行** PyGrading会自动迭代执行评测用例列表中的每个评测用例，而具体的评测规则可以用一个函数快速指定。

**评测结果处理** 通常包括评测结果汇总、生成评测报告、输出评测结果JSON串等任务。

在本文档这一部分接下来的内容中，将以一个普通编程题为例，创建一个评测内核并输出结果JSON串，样例题目如下：

> 题目名称：判断回文数  
> 问题描述：判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。  
> 示例 1:  
> 　　输入：121  
> 　　输出：True  
>
> 示例 2：  
> 　　输入：-121  
> 　　输出：False  
> 　　说明：从左向右为“-121”，从右向左为“121-”，故不是回文数。

本例使用的学生提交代码如下：
```python
def isPalindrome(num: int) -> bool:
    num = abs(num)
    num_str = str(num)
    return num_str == num_str[::-1]

x = eval(input())
print(isPalindrome(x))
```

本例使用的测试用例如下：
<table>
    <tr>
        <th>input</th>
        <th>output</th>
    </tr>
    <tr>
        <td>121</td>
        <td>True</td>
    </tr>
    <tr>
        <td>10</td>
        <td>False</td>
    </tr>
    <tr>
        <td>-12</td>
        <td>False</td>
    </tr>
    <tr>
        <td>331133</td>
        <td>True</td>
    </tr>
    <tr>
        <td>-121</td>
        <td>False</td>
    </tr>
</table>

> 样例学生代码在执行最后一组测试用例时会输出错误答案

#### 2. 导入程序包

PyGrading安装完成之后，推荐在您的代码中使用如下方式导入通用评测相关模块：

```python
import pygrading.general_test as gg
```

如果您需要在评测结果中显示html内容，推荐如下方式导入html相关模块：

```python
from pygrading.html import *
```

#### 3. 创建评测任务预处理函数

首先创建用于评测任务预处理的`prework()`函数，完成配置文件和评测用例的读取，配置文件使用JSON格式，内容如下：

```json
{
    "testcase_num": "5",
    "testcase_dir": "./example/testdata",
    "submit_path": "./example/submit/main.py"
}
```

PyGrading推荐按照如下目录结构构建评测数据，学生提交的代码将会被挂载到`submit`目录中，测试数据的输入输出存放于`testdata`目录中。PyGrading提供了函数可用于直接读取以这种目录结构创建的评测用例：

```
.
├── config.json
├── submit
│   └── main.py
└── testdata
    ├── input
    │   ├── input1.txt
    │   ├── input2.txt
    │   ├── input3.txt
    │   ├── input4.txt
    │   └── input5.txt
    └── output
        ├── output1.txt
        ├── output2.txt
        ├── output3.txt
        ├── output4.txt
        └── output5.txt
```

创建`prework()`函数的代码如下，`job`为PyGrading创建的任务实例：

```python
def prework(job):
    # 读取配置文件
    config = gg.load_config("./example/config.json")

    # 创建测试用例实例
    testcases = gg.create_std_testcase(config["testcase_dir"], config["testcase_num"])

    job.set_config(config)
    job.set_testcases(testcases)
```

#### 4. 创建评测用例执行函数

接下来创建创建用于执行测试用例的`run()`函数，该函数接收单组测试用例，并返回一个可包含任意内容的字典，所有评测用例返回的内容最终会汇总到一个列表中传递给评测结果处理函数。

使用`gg.utils.bash()`执行Shell命令时，会返回当前命令的执行时间，可用做代码性能评判依据。

创建`run()`函数的代码如下，`job`为PyGrading创建的任务实例，`testcase`为字典类型，包含单个测试用例信息：

```python
def run(job, testcase):
    # 读取当前任务的配置信息
    configuration = job.get_config()
    
    # 创建和执行评测用Shell命令
    cmd = ["cat", testcase.input_src, "|", "python3 " + configuration["submit_path"]]
    status, output, time = gg.utils.bash(" ".join(cmd))

    # 初始化返回的字典对象
    result = {"name": testcase.name, "time": time}
    
    # 读取评测用例答案
    answer = gg.utils.readfile(testcase.output_src)

    # 将执行结果写回返回对象
    result["output"] = output
    result["answer"] = answer

    # 比较评测答案和实际输出将评测结果写回返回对象
    if gg.utils.compare_str(output, answer):
        result["verdict"] = "Accept"
        result["score"] = testcase.score
    else:
        result["verdict"] = "Wrong Answer"
        result["score"] = 0

    return result
```

#### 5. 创建评测结果处理函数

之后创建评测结果处理函数`postwork()`，并使用`pygrading.html`中的相关工具创建带有HTML标签的字符串。

创建`postwork()`函数的代码如下，`job`为PyGrading创建的任务实例：

```python
def postwork(job):
    # 设定结果verdict
    job.verdict(str(font(color="green").set_text("Accept")))

    # 设定结果score
    job.score(job.get_total_score())

    # 设定结果rank
    job.rank({"rank": str(job.get_total_time())})

    # 创建HTML标签
    detail = table(
        tr(
            th(),
            th().set_text("Verdict"),
            th().set_text("Output"),
            th().set_text("Answer")
        ), border="0"
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

    # 将HTML标签转换为字符串，设定为结果detail
    job.detail(str(detail))
```

#### 6. 启动任务

完成三个阶段的函数编写后，将三个函数作为参数传入`gg.job()`函数，生成一个任务实例：

```python
# 创建任务实例
new_job = gg.job(prework=prework, run=run, postwork=postwork)

# 任务启动
new_job.start()

# 打印结果
new_job.print()
```

程序执行后输出结果如下：

```json
{"verdict": "<font color='red'>Wrong Answer</font>", "score": "80", "rank": {"rank": "238"}, "HTML": "enable", "detail": "<table border='1'><tr><th></th><th>Verdict</th><th>Output</th><th>Answer</th></tr><tr><td>TestCase1<br></td><td align='center'>Accept<br></td><td align='center'>True<br></td><td align='center'>True<br></td></tr><tr><td>TestCase2<br></td><td align='center'>Accept<br></td><td align='center'>False<br></td><td align='center'>False<br></td></tr><tr><td>TestCase3<br></td><td align='center'>Accept<br></td><td align='center'>False<br></td><td align='center'>False<br></td></tr><tr><td>TestCase4<br></td><td align='center'>Accept<br></td><td align='center'>True<br></td><td align='center'>True<br></td></tr><tr><td>TestCase5<br></td><td align='center'>Wrong Answer<br></td><td align='center'>True<br></td><td align='center'>False<br></td></tr></table>"}
```

在CG平台中显示效果如下：

<font color='red'>Wrong Answer</font>

<table border='0'>
    <tr>
        <th></th>
        <th>Verdict</th>
        <th>Output</th>
        <th>Answer</th>
    </tr>
    <tr>
        <td>TestCase1<br></td>
        <td align='center'>Accept<br></td>
        <td align='center'>True<br></td>
        <td align='center'>True<br></td>
    </tr>
    <tr>
        <td>TestCase2<br></td>
        <td align='center'>Accept<br></td>
        <td align='center'>False<br></td>
        <td align='center'>False<br></td>
    </tr>
    <tr>
        <td>TestCase3<br></td>
        <td align='center'>Accept<br></td>
        <td align='center'>False<br></td>
        <td align='center'>False<br></td>
    </tr>
    <tr>
        <td>TestCase4<br></td>
        <td align='center'>Accept<br></td>
        <td align='center'>True<br></td>
        <td align='center'>True<br></td>
    </tr>
    <tr>
        <td>TestCase5<br></td>
        <td align='center'>Wrong Answer<br></td>
        <td align='center'>True<br></td>
        <td align='center'>False<br></td>
    </tr>
</table>



