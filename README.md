PYTEST TUTORIAL
=============
[![python 2.7](https://img.shields.io/badge/python-2.7-brightgreen.svg)](https://www.python.org/)
[![pytest 3.6.4](https://img.shields.io/badge/pytest-3.6.4-green.svg)](https://docs.pytest.org/en/latest/)
[![allure_pytest 2.5.0](https://img.shields.io/badge/allure_pytest-2.5.0-yellow.svg)](https://github.com/allure-framework/allure-python)
[![pytest_html 1.19.0](https://img.shields.io/badge/pytest_html-1.19.0-yellowgreen.svg)](https://github.com/pytest-dev/pytest-html)
[![xdist 1.22.5](https://img.shields.io/badge/xdist-1.22.5-orange.svg)](https://pypi.org/project/pytest-xdist/)
[![Build Status](https://travis-ci.org/shashikumarraja/pytest_tutorial.svg?branch=master)](https://travis-ci.org/shashikumarraja/pytest_tutorial)

Contains pytest scripts which helps in understanding different pytest functionalities and features.

The [pytest](https://docs.pytest.org/en/latest/) framework makes it easy to write small tests, yet
scales to support complex functional testing for applications and libraries.

An example of a simple test:
```python
# content of test_sample.py
def inc(x):
    return x + 1
#make sure the test function's name starts with 'test_'
def test_answer():
    assert inc(3) == 5
```

To execute it::

    $ pytest
    ============================= test session starts =============================
    collected 1 items

    test_sample.py F

    ================================== FAILURES ===================================
    _________________________________ test_answer _________________________________

        def test_answer():
    >       assert inc(3) == 5
    E       assert 4 == 5
    E        +  where 4 = inc(3)

    test_sample.py:5: AssertionError
    ========================== 1 failed in 0.04 seconds ===========================

How to Run the project?
=====
1. Clone/download this repo

2. Install all the dependencies using-
```shell
pip install -r requirements.txt
```
To fix liniting errors the project uses [autopep8](https://github.com/hhatto/autopep8).

```shell
//To modify a file in place (with aggressive level 2):

$ autopep8 --in-place --aggressive --aggressive <filename>
```