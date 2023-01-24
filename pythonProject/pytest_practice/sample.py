# -- coding: utf-8 --
# import pytest


def func(x):
    return x+1


def test_func():
    assert func(3) == 5


def test_func1():
    assert func(7) > 8

