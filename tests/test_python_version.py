import unittest
import pytest
import sys

def test_python_version(unittest):
    print('python version test')
    assert sys.version == '3.7.16'

# content of test_sample.py
def test_answer(cmdopt):
    if cmdopt == "type1":
        print("first")
    elif cmdopt == "type2":
        print("second")
    assert 0  # to see what was printed