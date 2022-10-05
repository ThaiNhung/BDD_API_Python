#!/usr/bin/python
# -*- coding: utf-8 -*-

from behave import given, when, then
import requests


global_general_variables = {}
http_request_header = {}
http_request_body = {}
http_request_url_query_param = {}


@given(u'Set basic web application url is "{basic_app_url}"')
def step_impl(context, basic_app_url):
    global_general_variables['basic_application_URL'] = basic_app_url

@given(u'Set basic user details as "{particular}" and "{value}" below')
def step_impl(context, particular, value):
   for row in context.table:
        temp_value = row['value']
        global_general_variables[row['particular']] = temp_value
        if 'empty' in temp_value:
            global_general_variables[row['particular']] = ''

@given(u'Set GET api endpoint as "{get_api_endpoint}"')
def step_impl(context, get_api_endpoint):
    global_general_variables['GET_api_endpoint'] = get_api_endpoint


@when(u'Set HEADER param request content type as "{header_content_type}"')
def step_impl(context, header_content_type):
    http_request_header['content-type'] = header_content_type


@when(u'Set HEADER param response accept type as "{header_accept_type}"')
def step_impl(context, header_accept_type):
    http_request_header['content-type'] = header_accept_type
    
@when(u'Set Query param as "{query_param}"')
def step_impl(context, query_param):
    if 'empty' in query_param:
        http_request_url_query_param.clear()
    else:
        http_request_url_query_param.clear()
        http_request_url_query_param['signout_emailid'] = global_general_variables['email']
        http_request_url_query_param['session_id'] = global_general_variables['latest_session_key']

@when(u'Raise "{http_request_type}" HTTP request')
def step_impl(context, http_request_type):
    url_temp = global_general_variables['basic_application_URL']
    if 'GET' == http_request_type:
        url_temp += global_general_variables['GET_api_endpoint']
        http_request_body.clear()
        global_general_variables['response_full'] = requests.get(url_temp,
                                                                                         headers=http_request_header,
                                                                                         params=http_request_url_query_param,
                                                                                         data=http_request_body)

@then(u'Response http code should be {expected_response_code:d}')
def step_impl(context, expected_response_code):
    global_general_variables['expected_response_code'] = expected_response_code
    actual_response_code = global_general_variables['response_full'].status_code
    if str(actual_response_code) not in str(expected_response_code):
        print (str(global_general_variables['response_full'].json()))
        assert False, '***ERROR: Following unexpected error response code received: ' + str(actual_response_code)

@then(u'Response HEADER content type should be "{expected_response_content_type}"')
def step_impl(context, expected_response_content_type):
    global_general_variables['expected_response_content_type'] = expected_response_content_type
    actual_response_content_type = global_general_variables['response_full'].headers['Content-Type']
    if expected_response_content_type not in actual_response_content_type:
        assert False, '***ERROR: Following unexpected error response content type received: ' + actual_response_content_type

@then(u'Valid HTTP response should be received')
def step_impl(context):
    if None in global_general_variables['response_full']:
        assert False, 'Null response received'
        
@then(u'Response BODY should not be null or empty')
def step_impl(context):
    if None in global_general_variables['response_full']:
        assert False, '***ERROR:  Null or none response body received'

@then(u'Response BODY parsing for "{body_parsing_for}" should be successful')
def step_impl(context, body_parsing_for):
    current_json = global_general_variables['response_full'].json()
    if 'GET__signup' == body_parsing_for:
       print('Activity status               : ' + current_json['Additional message'])
       print('Additional message      : ' + current_json['Activity status'])
       print('Links                               : ')
       print('          Actual signup                                          : ' + current_json['Links'].get('Actual signup'))
       print('          Link documentation                               : ' + current_json['Links'].get('Actual signup'))
       print('Payload                          : ')
       print('          signup_emailid                                       : ' + current_json['Payload'].get('signup_emailid'))
       print('          signup_password                                   : ' + current_json['Payload'].get('signup_password'))
       print('          signup_firstname                                   : ' + current_json['Payload'].get('signup_firstname'))
       print('          signup_lastname                                    : ' + current_json['Payload'].get('signup_lastname'))
       print('          signup_gender                                       : ' + current_json['Payload'].get('signup_gender'))
       print('          signup_secret_question_1                   : ' + current_json['Payload'].get('signup_secret_question_1'))
       print('          signup_secret_question_2                   : ' + current_json['Payload'].get('signup_secret_question_2'))
       print('          signup_secret_question_1_answer    : ' + current_json['Payload'].get('signup_secret_question_1_answer'))
       print('          signup_secret_question_2_answer    : ' + current_json['Payload'].get('signup_secret_question_2_answer'))



#   behave --no-capture --no-capture-stderr