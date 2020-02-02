<h1 id="pygrading" align="center">PyGrading</h1>

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
	<a href="#change-log">Change Log</a> •
	<a href="#getting-start">Getting Start</a> •
	<a href="#api">API</a> •
	<a href="#tutorials">Tutorials</a> •
	<a href="http://www.educg.net/" target="_blank">CG Site</a>
</p>

<p align="center">
		<img src="./img/logo.png" width="200">
</p>

<h6 align="center">Made by Charles Zhang • :globe_with_meridians: <a href="https://github.com/PhenomingZ">https://github.com/PhenomingZ</a></h6>

<h2 id="what-is-it" align="center">What is it</h2>
<p align="right"><a href="#pygrading"><sup>▴ Back to top</sup></a></p>

**希冀平台** 是一个国内最具专业深度、安全可扩展的计算机类课程一体化支撑平台，是一个定位于全面支撑计算机、人工智能和大数据专业建设的大型综合教学实验平台，而非一个只能支撑若干门课程的实验系统。

**通用评测** 是一个通用的自动评测框架，基于该框架可以定制开发任何自己需要的自动评测内核。

**PyGrading工具包** 目前该工具包包含以下功能：
1. 支持CourseGrading平台通用评测内核快速构建；
2. 支持适用于通用评测题和虚拟桌面环境的评测结果JSON串的快速生成；
2. 支持HTML标签文本内容的快速生成，绝对好用的HTML生成工具；

希望使用本工具能够提高大家的工作效率，祝各位开发顺利！

<h2 id="install" align="center">Install</h2>
<p align="right"><a href="#pygrading"><sup>▴ Back to top</sup></a></p>

使用pip可以轻松安装PyGrading：

```bash
pip install pygrading
```

也可以下载项目文件后，切换到`setup.py`所在的目录，执行以下命令来安装：

```bash
python setup.py install
```

PyGrading的运行环境要求 **Python >= 3.6**，不支持Python2。

<h2 id="change-log" align="center">Change Log</h2>
<p align="right"><a href="#pygrading"><sup>▴ Back to top</sup></a></p>

**v0.1.2 Change Log (2020.02.01)**  
在`pygrading.heml`模块中添加了自定义标签方法`custom()`并支持形如`<input>`标签的不成组标签。

<details>
<summary>以往版本更新日志(点击以展开...)</summary>
<br>

**v0.1.0 Change Log (2020.01.29)**  
通用评测内核功能完成，HTML构建功能初步搭建完成。

</details>

<h2 id="getting-start" align="center">Getting Start</h2>
<p align="right"><a href="#pygrading"><sup>▴ Back to top</sup></a></p>

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
            td(align="center").set_text(str2html(i["name"])),
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
{"verdict": "<font color='red'>Wrong Answer</font>", "score": "80", "rank": {"rank": "238"}, "HTML": "enable", "detail": "<table border='1'><tr><th></th><th>Verdict</th><th>Output</th><th>Answer</th></tr><tr><td align='center'>TestCase1<br></td><td align='center'>Accept<br></td><td align='center'>True<br></td><td align='center'>True<br></td></tr><tr><td align='center'>TestCase2<br></td><td align='center'>Accept<br></td><td align='center'>False<br></td><td align='center'>False<br></td></tr><tr><td align='center'>TestCase3<br></td><td align='center'>Accept<br></td><td align='center'>False<br></td><td align='center'>False<br></td></tr><tr><td align='center'>TestCase4<br></td><td align='center'>Accept<br></td><td align='center'>True<br></td><td align='center'>True<br></td></tr><tr><td align='center'>TestCase5<br></td><td align='center'>Wrong Answer<br></td><td align='center'>True<br></td><td align='center'>False<br></td></tr></table>"}
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
        <td align='center'>TestCase1<br></td>
        <td align='center'>Accept<br></td>
        <td align='center'>True<br></td>
        <td align='center'>True<br></td>
    </tr>
    <tr>
        <td align='center'>TestCase2<br></td>
        <td align='center'>Accept<br></td>
        <td align='center'>False<br></td>
        <td align='center'>False<br></td>
    </tr>
    <tr>
        <td align='center'>TestCase3<br></td>
        <td align='center'>Accept<br></td>
        <td align='center'>False<br></td>
        <td align='center'>False<br></td>
    </tr>
    <tr>
        <td align='center'>TestCase4<br></td>
        <td align='center'>Accept<br></td>
        <td align='center'>True<br></td>
        <td align='center'>True<br></td>
    </tr>
    <tr>
        <td align='center'>TestCase5<br></td>
        <td align='center'>Wrong Answer<br></td>
        <td align='center'>True<br></td>
        <td align='center'>False<br></td>
    </tr>
</table>

一个简单的通用评测内核开发完成！

<h2 id="api" align="center">PyGrading API</h2>
<p align="right"><a href="#pygrading"><sup>▴ Back to top</sup></a></p>

在本节中，将会列出当前版本(v0.1.2)全部的接口与方法，详细使用方法请参考<a href="#tutorials">Tutorials</a>部分。

### pygrading.general_test

该包推荐导入方式：

```python
import pygrading.general_test as gg
```

包含有以下方法和类：

#### 1. gg.load_config(source: str)  

> 读取含有配置信息的JSON文件，返回字典类型。

<details>
<summary>详细信息(点击以展开...)</summary>
<br>

<b>Arguments:</b>
<table>
    <tr>
        <th>Arguments</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>source</td>
        <td>String</td>
        <td>Required</td>
        <td>配置文件的文件路径</td>
    </tr>
</table>

<b>Returns:</b>
<table>
    <tr>
        <th>Type</th>
        <th>Description</th>
        <th>Example</th>
    </tr>
    <tr>
        <td>Dict</td>
        <td>以字典形式返回配置信息</td>
        <td>{'testcase_num': '3','testcase_dir': 'example/testdata','submit_path': 'example/submit/*'}</td>
    </tr>
</table>
</details>

#### 2. gg.create_std_testcase(testcase_dir: str, testcase_num: int) 
 
> 以推荐的方式创建TestCases对象实例。

<details>
<summary>详细信息(点击以展开...)</summary>
<br>

以推荐的方式构建评测用例目录，即可使用本方法直接创建一个TestCases对象实例。

推荐的目录构建方式如下：

```
testdata
├── input
│   ├── input1.txt
│   ├── input2.txt
│   └── input3.txt
└── output
    ├── output1.txt
    ├── output2.txt
    └── output3.txt
```

testdata目录为评测用例所在的根目录，评测用例的输入和输出分别放在input和output两个子目录中。

所有的评测用例输入按照input1.txt、input2.txt、input3.txt依次命名，所有的评测用例输出按照output1.txt、output2.txt、output3.txt依次命名。

<b>Arguments:</b>
<table>
    <tr>
        <th>Arguments</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>testcase_dir</td>
        <td>String</td>
        <td>Required</td>
        <td>评测用例目录路径</td>
    </tr>
    <tr>
        <td>testcase_num</td>
        <td>Integer</td>
        <td>Required</td>
        <td>评测用例的数目</td>
    </tr>
</table>

<b>Returns:</b>
<table>
    <tr>
        <th>Type</th>
        <th>Description</th>
        <th>Example</th>
    </tr>
    <tr>
        <td>TestCases</td>
        <td>PyGrading创建的评测用例实例类型</td>
        <td>-</td>
    </tr>
</table>
</details>

#### 3. gg.create_testcase(total_score: int = 100)  

> 创建一个空的TestCases实例。

<details>
<summary>详细信息(点击以展开...)</summary>
<br>

在无法使用推荐的方式构建评测用例的情况下，可以创建一个空的TestCases实例并手动添加评测用例。添加方法请参考`gg.TestCases`类的介绍。

<b>Arguments:</b>
<table>
    <tr>
        <th>Arguments</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>total_score</td>
        <td>Integer</td>
        <td>100</td>
        <td>评测用例总分</td>
    </tr>
</table>

<b>Returns:</b>
<table>
    <tr>
        <th>Type</th>
        <th>Description</th>
        <th>Example</th>
    </tr>
    <tr>
        <td>TestCases</td>
        <td>PyGrading创建的评测用例实例类型</td>
        <td></td>
    </tr>
</table>
</details>

#### 4. gg.TestCases 类

> 该类用于存储和传递关于评测用例的全部信息，通过迭代的方式将每个测试用例传入到评测用例执行函数中。  
> 请使用`gg.create_std_testcase()`或`gg.create_testcase()`获取TestCases实例。

<details>
<summary>详细信息(点击以展开...)</summary>
<br>

`gg.TestCases`类包含有1个子类`__SingleTestCase`，该子类的实例用于存储单个评测用例的信息，且会作为一个必要参数传入评测用例执行函数中。

子类`__SingleTestCase`包含的属性如下：

<table>
    <tr>
        <th>Attributes</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>name</td>
        <td>String</td>
        <td>Required</td>
        <td>评测用例的名称</td>
    </tr>
    <tr>
        <td>score</td>
        <td>Integer</td>
        <td>Required</td>
        <td>评测用例的满分分值</td>
    </tr>
    <tr>
        <td>input_src</td>
        <td>Object</td>
        <td>Required</td>
        <td>评测用例的输入，可以为任何类型</td>
    </tr>
    <tr>
        <td>output_src</td>
        <td>Object</td>
        <td>Required</td>
        <td>评测用例的输出，可以为任何类型</td>
    </tr>
    <tr>
        <td>extension</td>
        <td>Object</td>
        <td>None</td>
        <td>评测用例的额外信息，可以为任何类型</td>
    </tr>
</table>

`gg.TestCases`类包含有如下属性：

<table>
    <tr>
        <th>Attributes</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>__count</td>
        <td>Integer</td>
        <td>0</td>
        <td>保存该实例中评测用例的数量</td>
    </tr>
    <tr>
        <td>__cases</td>
        <td>List</td>
        <td>[ ]</td>
        <td>以列表的形式保存实例中所有的评测用例</td>
    </tr>
    <tr>
        <td>__total_score</td>
        <td>Integer</td>
        <td>100</td>
        <td>保存评测用例总分，默认为百分制</td>
    </tr>
</table>


`gg.TestCases`类包含有如下方法：

<table>
    <tr>
        <th>Function</th>
        <th>Return</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>TestCases.append(self, name: str, score: float, input_src: object, output_src: object, extension: object = None)</td>
        <td>None</td>
        <td>向一个TestCases实例添加评测用例，传入参数的属性和<code>__SingleTestCase</code>中对应</td>
    </tr>
    <tr>
        <td>TestCases.get_count(self)</td>
        <td>Integer</td>
        <td>获取评测用例数目值</td>
    </tr>
    <tr>
        <td>TestCases.get_total_score(self)</td>
        <td>Integer</td>
        <td>获取评测用例总分</td>
    </tr>
    <tr>
        <td>TestCases.get_testcases(self)</td>
        <td>List[__SingleTestCase]</td>
        <td>获取评测用例列表</td>
    </tr>
    <tr>
        <td>TestCases.set_total_score(self, total_score: int)</td>
        <td>None</td>
        <td>设定评测用例总分</td>
    </tr>
    <tr>
        <td>TestCases.isempty(self)</td>
        <td>Boolean</td>
        <td>判断评测用例是否为空</td>
    </tr>
</table>
</details>

#### 5. gg.job(prework=None, run=None, postwork=None)

> 该方法用于创建评测任务实例，传入评测任务预处理、评测用例执行、评测结果处理的相关函数，返回一个Job实例。   

<details>
<summary>详细信息(点击以展开...)</summary>
<br>

<b>Arguments:</b>
<table>
    <tr>
        <th>Arguments</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>prework</td>
        <td>Function</td>
        <td>None</td>
        <td>评测任务预处理函数</td>
    </tr>
    <tr>
        <td>run</td>
        <td>Function</td>
        <td>None</td>
        <td>评测用例执行函数</td>
    </tr>
    <tr>
        <td>postwork</td>
        <td>Function</td>
        <td>None</td>
        <td>评测结果处理函数</td>
    </tr>
</table>

<b>Returns:</b>
<table>
    <tr>
        <th>Type</th>
        <th>Description</th>
        <th>Example</th>
    </tr>
    <tr>
        <td>Job</td>
        <td>PyGrading创建的评测任务实例类型</td>
        <td></td>
    </tr>
</table>
</details>

#### 6. gg.Job 类

> 该类用于创建评测任务实例，提供任务初始化、任务执行、输出结果的功能。   

<details>
<summary>详细信息(点击以展开...)</summary>
<br>

`gg.Job`类包含有如下属性：

<table>
    <tr>
        <th>Attributes</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>__prework</td>
        <td>Function</td>
        <td>None</td>
        <td>评测任务预处理函数</td>
    </tr>
    <tr>
        <td>__run</td>
        <td>Function</td>
        <td>None</td>
        <td>评测用例执行函数</td>
    </tr>
    <tr>
        <td>__postwork</td>
        <td>Function</td>
        <td>None</td>
        <td>评测结果处理函数</td>
    </tr>
    <tr>
        <td>__testcases</td>
        <td>TestCases</td>
        <td>TestCases()</td>
        <td>评测用例</td>
    </tr>
    <tr>
        <td>__config</td>
        <td>Dict</td>
        <td>None</td>
        <td>配置信息</td>
    </tr>
    <tr>
        <td>__terminate</td>
        <td>Boolean</td>
        <td>False</td>
        <td>程序结束标记</td>
    </tr>
    <tr>
        <td>__result</td>
        <td>Dict</td>
        <td>{<br>
            "verdict": "Unknown Error",<br>
            "score": "0",<br>
            "rank": {"rank": "-1"},<br>
            "HTML": "enable"<br>
        }</td>
        <td>评测任务执行结果的内部存储字典</td>
    </tr>
    <tr>
        <td>__summary</td>
        <td>List</td>
        <td>[ ]</td>
        <td>每个测试用例的执行结果汇总列表</td>
    </tr>
</table>

`gg.Job`类包含有如下方法：

<table>
    <tr>
        <th>Function</th>
        <th>Return</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>Job.verdict(self, src: str)</td>
        <td>None</td>
        <td>修改返回结果中的verdict字段</td>
    </tr>
    <tr>
        <td>Job.score(self, src: int)</td>
        <td>None</td>
        <td>修改返回结果中的score字段</td>
    </tr>
    <tr>
        <td>Job.rank(self, src: Dict)</td>
        <td>None</td>
        <td>修改返回结果中的rank字段</td>
    </tr>
    <tr>
        <td>Job.images(self, src: str)</td>
        <td>None</td>
        <td>修改返回结果中的images字段</td>
    </tr>
    <tr>
        <td>Job.comment(self, src: str)</td>
        <td>None</td>
        <td>修改返回结果中的comment字段</td>
    </tr>
    <tr>
        <td>Job.detail(self, src: str)</td>
        <td>None</td>
        <td>修改返回结果中的detail字段</td>
    </tr>
    <tr>
        <td>Job.detail(self, src: str)</td>
        <td>None</td>
        <td>修改返回结果中的detail字段</td>
    </tr>
    <tr>
        <td>Job.HTML(self, src: str)</td>
        <td>None</td>
        <td>修改返回结果中的HTML字段</td>
    </tr>
    <tr>
        <td>Job.custom(self, key: str, value: str)</td>
        <td>None</td>
        <td>在返回结果中创建自定义字段并赋值</td>
    </tr>
    <tr>
        <td>Job.get_summary(self)</td>
        <td>List</td>
        <td>获取评测用例汇总结果列表</td>
    </tr>
    <tr>
        <td>Job.get_config(self)</td>
        <td>Dict</td>
        <td>获取评测任务配置信息</td>
    </tr>
    <tr>
        <td>Job.get_total_score(self)</td>
        <td>Integer</td>
        <td>获取评测任务总分</td>
    </tr>
    <tr>
        <td>Job.get_total_time(self)</td>
        <td>Integer</td>
        <td>获取评测任务执行总时间</td>
    </tr>
    <tr>
        <td>Job.set_testcases(self, testcases: TestCases)</td>
        <td>None</td>
        <td>设定评测任务的评测用例</td>
    </tr>
    <tr>
        <td>Job.set_config(self, config: Dict)</td>
        <td>None</td>
        <td>设定评测用例的配置信息</td>
    </tr>
    <tr>
        <td>Job.terminate(self)</td>
        <td>None</td>
        <td>将终止标记置于True，执行完当前函数后评测终止</td>
    </tr>
    <tr>
        <td>Job.start(self)</td>
        <td>List</td>
        <td>开始任务，返回评测用例汇总结果列表</td>
    </tr>
    <tr>
        <td>Job.print(self)</td>
        <td>None</td>
        <td>将评测结果转化为JSON格式并打印到标准输出</td>
    </tr>
</table>
</details>

### pygrading.general_test.utils

该包封装了在编写评测内核的过程中可能会使用到的基本操作，可分为如下几类：

#### 1. 执行操作  

> 执行Shell命令的方法，返回值包括执行状态、执行后输出的内容、执行时间。

<details>
<summary>详细信息(点击以展开...)</summary>
<br>

<table>
    <tr>
        <th>Function</th>
        <th>Return</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>gg.utils.bash(cmd: str)</td>
        <td>Tuple</td>
        <td>执行Shell命令，返回值包括执行状态(status)、执行后输出的内容(output)、执行时间(time)</td>
    </tr>
</table>
</details>

#### 2. 文件操作  

> 有关文件读写增删的相关操作。

<details>
<summary>详细信息(点击以展开...)</summary>
<br>

<table>
    <tr>
        <th>Function</th>
        <th>Return</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>gg.utils.copyfile(src: str, dst: str)</td>
        <td>None</td>
        <td>将src路径所指示的文件复制到dst所指示的位置</td>
    </tr>
    <tr>
        <td>gg.utils.copytree(src: str, dst: str)</td>
        <td>None</td>
        <td>将src路径所指示的目录递归地复制到dst所指示的位置</td>
    </tr>
    <tr>
        <td>gg.utils.move(src: str, dst: str)</td>
        <td>None</td>
        <td>将src路径所指示的文件移动到dst所指示的位置</td>
    </tr>
    <tr>
        <td>gg.utils.rmtree(src: str)</td>
        <td>None</td>
        <td>递归地删除src路径所指示的目录</td>
    </tr>
    <tr>
        <td>gg.utils.rmfile(src: str)</td>
        <td>None</td>
        <td>删除src路径所指示的文件</td>
    </tr>
    <tr>
        <td>gg.utils.rename(old: str, new: str)</td>
        <td>None</td>
        <td>将old路径所指示的文件重命名为new</td>
    </tr>
    <tr>
        <td>gg.utils.readfile(src: str)</td>
        <td>String</td>
        <td>读取路径为src的文件，并以字符串的形式返回文件内容，文件中的换行以'\n'表示</td>
    </tr>
    <tr>
        <td>gg.utils.writefile(src: str, lines: str, option: str = "w")</td>
        <td>None</td>
        <td>将lines中的内容写入src，通过option选项选择写入模式，默认为“w”</td>
    </tr>
    <tr>
        <td>gg.utils.readfile_list(src: str)</td>
        <td>List[str]</td>
        <td>读取路径为src的文件，并以列表的形式返回文件内容，文件中每行为列表中的一个元素</td>
    </tr>
    <tr>
        <td>gg.utils.writefile_list(src: str, lines: List, option: str = "w")</td>
        <td>None</td>
        <td>将lines中的内容写入src，通过option选项选择写入模式，默认为"w"</td>
    </tr>
    <tr>
        <td>gg.utils.str2list(src: str)</td>
        <td>List[str]</td>
        <td>将普通字符串转化为列表，根据"\n"进行分隔，并会自动去掉字符串末尾的空行</td>
    </tr>
</table>
</details>

#### 3. 比较操作  

> 关于评测用例执行结果比较打分的相关操作。

<details>
<summary>详细信息(点击以展开...)</summary>
<br>

<table>
    <tr>
        <th>Function</th>
        <th>Return</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>gg.utils.compare_str(str1: str, str2: str)</td>
        <td>Boolean</td>
        <td>返回输入的两个字符串是否相同，并自动忽略字符串尾的换行符</td>
    </tr>
    <tr>
        <td>gg.utils.compare_list(list1: List, list2: List)</td>
        <td>Boolean</td>
        <td>返回输入的两个列表是否相同，并自动忽略列表最后的换行符和空白字符串</td>
    </tr>
    <tr>
        <td>gg.utils.edit_distance(obj1, obj2)</td>
        <td>Integer</td>
        <td>返回两个可迭代类型的参数是否相同，在比较字符串和列表时不会自动处理空行，建议在进行字符串比较时，使用<code>str2list()函数</code>预处理传入的数据</td>
    </tr>
</table>
</details>

### pygrading.general_test.compiler

该包封装了部分编程语言的编译方法，目前支持如下编程语言：

> c, cpp

包含的方法如下：

<details>
<summary>详细信息(点击以展开...)</summary>
<br>

<table>
    <tr>
        <th>Function</th>
        <th>Return</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>gg.compiler.compile_c(source: str, target: str, compiler_type: str = "gcc", option: str = "-O2 -Wall -std=c99")</td>
        <td>Tuple</td>
        <td>针对c语言编译的方法，通过source传入源文件路径，target指定编译后文件路径，compiler_type选择编译器类型，通过option添加编译选项。返回执行状态和执行过程中的输出</td>
    </tr>
    <tr>
        <td>gg.compiler.compile_cpp(source: str, target: str, compiler_type: str = "g++", option: str = "-O2 -Wall -std=c++11")</td>
        <td>Tuple</td>
        <td>针对c++语言编译的方法，通过source传入源文件路径，target指定编译后文件路径，compiler_type选择编译器类型，通过option添加编译选项。返回执行状态和执行过程中的输出</td>
    </tr>
</table>
</details>

<h2 id="tutorials" align="center">Tutorials</h2>
<p align="right"><a href="#pygrading"><sup>▴ Back to top</sup></a></p>


