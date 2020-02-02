import pygrading.general_test as gg
from pygrading.html import *

a = table(
    tr(
        td(font(color="red").set_text("Hello World"))
    )
)

b = [tr(), tr()]

a.extend(b)

print(a)