from pygrading.html import *

# 在括号中可以输入任意组键值对，他们将作为标签的属性显示在最终的HTML文本中
accept = font(color="green").set_text("Accept")
wrong_answer = font(color="red").set_text("Wrong Answer")

accept.print()
wrong_answer.print()