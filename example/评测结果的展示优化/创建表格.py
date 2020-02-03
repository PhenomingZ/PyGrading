from pygrading.html import *

# 可以看到字符串中含有换行符，推荐使用str2html()函数进行处理，将换行符转化为<br>
outputs = ["1", "1\n2", "1\n2\n3", "1\n2\n3\n4", "5\n4\n3\n2\n1"]
answers = ["1", "1\n2", "1\n2\n3", "1\n2\n3\n4", "1\n2\n3\n4\n5"]

# 标签之间可以相互嵌套，任意数量的子标签可以作为参数传递给父标签
result = table(
    tr(
        th().set_text("Output"),
        th().set_text("Answer")
    )
)

for out, ans in zip(outputs, answers):
    tmp = tr(
        td().set_text(str2html(out)),
        td().set_text(str2html(ans)),
    )
    # 可以使用“<<”操作符将一个标签作为子标签传递给另一个标签
    result << tmp

result.print()