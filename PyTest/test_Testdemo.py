# Running command in terminal:
# pytest -v -s
# pytest -v -s test_Testdemo.py

# When using pytest, it is very important PyTest Naming Conventions.
# If we don't follow naming conventions then it will not pick up tests from the file.
# File names should start as test_example.py or example_test.py


import pytest

def testMethod1():
    print("This is test method1.")

def testMethod2():
    print("This is test method2")