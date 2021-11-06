import pytest
import requests
import json

from client import Task_rest


# def test_get_from_empty_numbered_queue():
#     url = "http://localhost:8888"
#     queue = 10000
#
#     GetRequest = Task_rest(url)
#     get_request_result = GetRequest.get(queue)
#     message = (json.loads(get_request_result.text)['message'])
#
#     '''
#     Summary: Check get request to empty numbered queue
#
#     Precondition:
#
#     Steps:                                                                      Result:
#     1.   Set value to url (e.g. "http://localhost:8888")
#
#     2. Set value to queue (e.g. 10000)
#
#     3. Run get-request with parameter_for_query = {'queue': queue_number}
#
#     Expected result: text from responce: "no messages"
#
#     '''
#
#     assert message == "no messages"

def test_post_to_empty_numbered_queue():
    url = "http://localhost:8888"
    queue = 10000
    number_of_messages = 3
#    post_request_result = PostRequest.post(queue, message)
    numbers = list(range(1, number_of_messages + 1))
    messages = []
    for num in numbers:
        messages.append("text_" + str(num))

    messages_from_client = []
    PostRequest = Task_rest(url)
    for i in range(0, number_of_messages):
        message_from_client = messages[i]
        post_request_result = PostRequest.post(queue, message_from_client[i])
        if post_request_result.status_code == 201:
            messages_from_client.append(messages[i])

    messages_from_get = []
    GetRequest = Task_rest(url)
    get_request_result = GetRequest.get(queue)
    for i in range(1, number_of_messages + 1):
        if get_request_result.status_code == 200:
            message = json.loads(get_request_result.text)['message']

            messages_from_get.append(message)

    '''
    Summary: Check API for 'Message exchange framework for numbered queue'

    Precondition:

    Steps:                                                                      Result:
    1.   Set value to url (e.g. "http://localhost:8888")                       url = "http://localhost:8888"

    2. Set value to queue_number (e.g. 10000)                                  queue_number = 10000

    3. Run post-request with
       parameter_for_query = {"message": "text_1", "queue": queue_number}

    Expected result:  Status_code = 201
    '''

    assert messages_from_client == messages_from_get
#
# def test_post_to_numbered_queue_with_messages():
#
#     parameter_for_query = {"message": "text_2", "queue": queue_number}
#     task_post = Task_rest(url, parameter_for_query)
#     query_post = task_post.post()
#     '''
#     Summary: Check API for 'Message exchange framework for numbered queue'
#
#     Precondition:
#
#     Steps:                                                                      Result:
#     1.   Set value to url (e.g. "http://localhost:8888")                       url = "http://localhost:8888"
#
#     2. Set value to queue_number (e.g. 10000)                                  queue_number = 10000
#
#     4. Run post-request with
#        parameter_for_query = {"message": "text_1", "queue": queue_number}      Status_code = 201
#
#     5. Run post-request with
#        parameter_for_query = {"message": "text_2", "queue": queue_number}      Status_code = 201
#
#     6. Run post-request with
#        parameter_for_query = {"message": "text_3", "queue": queue_number}      Status_code = 201
#
#     8. Run get-request with
#        parameter_for_query = {"queue": queue_number}
#
#     Expected result: text from response "text_1"
#
#     '''
#
#     assert
#
# def test_get_oldest_message_from_numbered_queue():
#
#     parameter_for_query = {'queue': queue_number}
#     task_get = Task_rest(url, parameter_for_query)
#     query_get = task_get.get()
#     message = query_get.text
#     assert message_text_from_response(message) == "text_1"
#
# def test_delete_from_numbered_queue():
#
#     parameter_for_query = {'queue': queue_number}
#     task_delete = Task_rest(url, parameter_for_query)
#     query_delete = task_delete.delete()
#     assert query_delete.status_code == 204
#
# def test_that_oldest_message_was_deleted_from_numbered_queue():
#
#     parameter_for_query = {'queue': queue_number}
#     task_get = Task_rest(url, parameter_for_query)
#     query_get = task_get.get()
#     message = query_get.text
#     assert message_text_from_response(message) == "text_3"
#
# def test_that_oldest_message_was_deleted_after_get_request_from_numbered_queue():
#
#     parameter_for_query = {'queue': queue_number}
#     task_get = Task_rest(url, parameter_for_query)
#     query_get = task_get.get()
#     message = query_get.text
#
#     '''
#         Summary: Check API for 'Message exchange framework for numbered queue'
#
#         Precondition:
#
#         Steps:                                                                      Result:
#         1.   Set value to url (e.g. "http://localhost:8888")                       url = "http://localhost:8888"
#
#         2. Set value to queue_number (e.g. 10000)                                  queue_number = 10000
#
#         3. Run get-request with parameter_for_query = {'queue': queue_number}      Text from responce: "no messages"
#
#         4. Run post-request with
#            parameter_for_query = {"message": "text_1", "queue": queue_number}      Status_code = 201
#
#         5. Run post-request with
#            parameter_for_query = {"message": "text_2", "queue": queue_number}      Status_code = 201
#
#         6. Run post-request with
#            parameter_for_query = {"message": "text_3", "queue": queue_number}      Status_code = 201
#
#         7. Run put-request with
#            parameter_for_query = {"message": "changed_message",
#                                    "queue": queue_number}                          Status_code = 201
#
#         8. Run get-request with
#            parameter_for_query = {"queue": queue_number}                           Text from responce: "changed_message"
#
#         9. Run delete-request with
#            parameter_for_query = {"queue": queue_number}                           Status_code = 204
#
#         10. Run get-request with
#            parameter_for_query = {"queue": queue_number}                           Text from responce: "text_3"
#
#         11. Run get-request with
#            parameter_for_query = {"queue": queue_number}                           Text from responce: "no messages"
#         '''
#     assert message_text_from_response(message) == "no messages"
