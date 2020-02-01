from pygrading.html import *

a = html(
    input_tag(type="text", name="email", size="40", maxlength="50"),
    input_tag(type="password"),
    input_tag(type="checkbox", checked="checked"),
    table(
        tr(
            td().set_text("123"),
            td().set_text("456")
        ),
        tr(
            td().set_text("789"),
            td().set_text("!@#")
        )
    )
)

a.print()