"""
    Name: setup.py
    Author: Charles Zhang <694556046@qq.com>
    Propose: Setup script for pygrading!
    Coding: UTF-8
"""

# 在setup.py的目录下，每次提交记得修改版本号，并删除之前生成的文件
# python3 setup.py sdist bdist_wheel
# python3 -m twine upload dist/*

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pygrading",
    version="0.4.2",
    author="Charles Zhang",
    author_email="694556046@qq.com",
    description="A Python ToolBox for CourseGrading platform.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PhenomingZ/PyGrading",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        'Jinja2>=2.10',
    ],
)
