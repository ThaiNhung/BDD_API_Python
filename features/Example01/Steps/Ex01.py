from behave import given, when, then
import os
import sys


@given(u'I confident with my experience')
def step_impl(context):
    print ('precondition for interview')


@when(u'I interviewed')
def step_impl(context):
    print ('waitting result')


@then(u'will recieve the result passed')
def step_impl(context):
    print ('passed if ok')

@then(u'if I do not have knowledge I will failed')
def step_impl(context):
    print ('failed if not ok')

#  cd D:\Automation_project\Python_Projects\Python_Behave_Demo\Demo1_GettingStarted\Sample1
#  behave
#  behave --no-capture --no-capture-stderr
