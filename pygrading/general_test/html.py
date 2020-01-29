"""
    Name: html.py
    Author: Charles Zhang <694556046@qq.com>
    Propose: A module to generate html code.
    Coding: UTF-8

    Change Log:
        **2020.01.29**
        Create this file!
"""


def str2html(src: str) -> str:
    """Switch normal string to a html type"""
    str_list = src.split("\n")
    while str_list[-1] == "\n" or str_list[-1] == "":
        str_list.pop()

    for i in range(len(str_list)):
        str_list[i] += "<br>"

    return "".join(str_list)


class Tag(object):
    """Tag

    A super class of all html tag class.

    Attributes:
        name: Tag name.
        subtag: Sub tags.
        attributes: Attributes of this tag.
    """

    def __init__(self):
        pass
