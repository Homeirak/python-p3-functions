#!/usr/bin/env python3

# def my_function(param):
#     print("Running my_function")
#     return param + 1

# The return keyword will disrupt the execution of your function, and prevent Python from running any lines of code after the return keyword.

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return num1 + num2

def halve(number):
    return number/2
