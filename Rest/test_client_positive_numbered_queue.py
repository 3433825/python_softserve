import pytest
import requests
from client import Task_rest
from client import message_text_from_response
'''
Summary: Check API for 'Message exchange framework for numbered queue'

Precondition:

Steps:                                                                      Result:
1.   Set value to url (e.g. "http://localhost:8888")                       url = "http://localhost:8888"                              

2. Set value to queue_number (e.g. 10000)                                  queue_number = 10000

3. Run get-request with parameter_for_query = {'queue': queue_number}      Text from responce: "no messages" 

4. Run post-request with 
   parameter_for_query = {"message": "text_1", "queue": queue_number}      Status_code = 201

5. Run post-request with 
   parameter_for_query = {"message": "text_2", "queue": queue_number}      Status_code = 201 

6. Run post-request with 
   parameter_for_query = {"message": "text_3", "queue": queue_number}      Status_code = 201

7. Run put-request with 
   parameter_for_query = {"message": "changed_message",
                           "queue": queue_number}                          Status_code = 201

8. Run get-request with 
   parameter_for_query = {"queue": queue_number}                           Text from responce: "changed_message" 

9. Run delete-request with 
   parameter_for_query = {"queue": queue_number}                           Status_code = 204
 
10. Run get-request with 
   parameter_for_query = {"queue": queue_number}                           Text from responce: "text_3"

11. Run get-request with 
   parameter_for_query = {"queue": queue_number}                           Text from responce: "no messages"
'''

url = "http://localhost:8888"

queue_number = 10000

def test_get_from_empty_numbered_queue():

    parameter_for_query = {'queue': queue_number}
    task_get = Task_rest(url, parameter_for_query)
    query_get = task_get.get()
    message = query_get.text
    assert message_text_from_response(message) == "no messages"

def test_post_to_empty_numbered_queue():

    parameter_for_query = {"message": "text_1", "queue": queue_number}
    task_post = Task_rest(url, parameter_for_query)
    query_post = task_post.post()
    assert query_post.status_code == 201

def test_post_to_numbered_queue_with_messages():

    parameter_for_query = {"message": "text_2", "queue": queue_number}
    task_post = Task_rest(url, parameter_for_query)
    query_post = task_post.post()
    assert query_post.status_code == 201

    parameter_for_query = {"message": "text_3", "queue": queue_number}
    task_post = Task_rest(url, parameter_for_query)
    query_post = task_post.post()
    assert query_post.status_code == 201

def test_get_oldest_message_from_numbered_queue():

    parameter_for_query = {'queue': queue_number}
    task_get = Task_rest(url, parameter_for_query)
    query_get = task_get.get()
    message = query_get.text
    assert message_text_from_response(message) == "text_1"

def test_delete_from_numbered_queue():

    parameter_for_query = {'queue': queue_number}
    task_delete = Task_rest(url, parameter_for_query)
    query_delete = task_delete.delete()
    assert query_delete.status_code == 204

def test_that_oldest_message_was_deleted_from_numbered_queue():

    parameter_for_query = {'queue': queue_number}
    task_get = Task_rest(url, parameter_for_query)
    query_get = task_get.get()
    message = query_get.text
    assert message_text_from_response(message) == "text_3"

def test_that_oldest_message_was_deleted_after_get_request_from_numbered_queue():

    parameter_for_query = {'queue': queue_number}
    task_get = Task_rest(url, parameter_for_query)
    query_get = task_get.get()
    message = query_get.text
    assert message_text_from_response(message) == "no messages"
