import unittest
import pytest
import sys

def test_python_version(unittest):
    print('python version test')
    assert sys.version == '3.7.16'

