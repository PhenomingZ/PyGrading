from pygrading.general_test.testcase import TestCases
from typing import Dict, List
import json


# noinspection PyBroadException
class Job(object):
    """Job

    A Job is a work flow, using run() function to handle each testcase.

    Attributes:
        __run: A function can handle each testcase.
        __testcases: An list of test cases.
        __config: A dict of config information.
        __result: A dict of grading result.For Example:
                {
                    "verdict":"可选，基本判定，一般为简要的评测结果描述或者简写，例如OJ系统的AC、PE、CE等",
                    "rank":{
                        "rank":"选择排行榜模式时，必须有该项，浮点数(正常值 ≥0)，该值决定了本次提交在排行榜上的位置，
                                排行榜从小到大排序。该rank可能来自后面几个值（value1、 value2、......）的加权。
                                如果提交的材料有误或者其它异常，将rank值置为负数，不参与排行!"，
                        "key1":"value1，可选，字符串，显示在排行榜上，Key1作为表头"，
                        "key2":"value2，可选，字符串，显示在排行榜上，Key2作为表头"，
                        ......
                    },
                    "score":"选择直接评测得分时，必须有该项，按照百分制给分，必须为大于等于0的整数，例如90",
                    "images":["可选，如果评测结果有图表，需要转换为base64或者SVG(启用HTML)格式", "图片2"],
                    "comment":"可选，评测结果的简要描述。",
                    "detail":"可选，评测结果的详细描述，可以包含协助查错的信息。布置作业的时候，可以选择是否显示这项信息。",
                    "secret":"可选，该信息只有教师评阅时才能看到。",
                    "HTML":"可选，如果置为enable，开发者可以使用HTML标签对verdict、comment、detail的输出内容进行渲染。"
                 }
    """

    def __init__(self, run, testcases: TestCases, config: Dict):
        """Init Job instance"""
        self.__run = run
        self.__testcases = testcases
        self.__config = config
        self.__result = {
            "verdict": "Unknown Error",
            "score": "0",
            "rank": {"rank": "-1"},
            "HTML": "enable"
        }
        self.__summary = []

    def verdict(self, src: str):
        self.__result["verdict"] = src

    def score(self, src: int):
        self.__result["score"] = str(src)

    def rank(self, src: Dict):
        self.__result["rank"] = src

    def images(self, src: str):
        self.__result["images"] = src

    def comment(self, src: str):
        self.__result["comment"] = src

    def detail(self, src: str):
        self.__result["detail"] = src

    def HTML(self, src: str):
        self.__result["HTML"] = src

    def get_summary(self):
        return self.__summary

    def get_total_score(self):
        ret = 0
        for i in self.__summary:
            if type(i) == dict and "score" in i:
                ret += float(i["score"])
        return int(ret)

    def get_total_time(self):
        ret = 0
        for i in self.__summary:
            if type(i) == dict and "time" in i:
                ret += int(i["time"])
        return int(ret)

    def start(self) -> List:
        """Start a job and return summary"""
        testcases = self.__testcases.get_testcases()
        for case in testcases:
            try:
                ret = self.__run(case, self.__config)
                self.__summary.append(ret)
            except Exception as e:
                self.__summary.append({
                    "name": case.name,
                    "score": 0,
                    "verdict": "Runtime Error",
                    "output": str(e)
                })
        return self.get_summary()

    def print(self):
        str_json = json.dumps(self.__result)
        print(str_json)


def job(run, testcases: TestCases, config: Dict):
    return Job(run, testcases, config)
