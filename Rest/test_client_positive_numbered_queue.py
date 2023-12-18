import pytest
import requests
import json

from client import Client

#@pytest.fixture()
def creating_list_of_messages(number_of_messages):
    numbers = list(range(1, number_of_messages + 1))
    messages = []
    for num in numbers:
        messages.append("text_" + str(num))
    return messages

def test_get_from_empty_numbered_queue():
    url = "http://localhost:8888"
    queue = 1

    GetRequest = Client(url)
    get_request_result = GetRequest.get(queue)
    get_request_status_code = get_request_result.status_code
    get_request_status_reason = get_request_result.reason
    message = (json.loads(get_request_result.text)['message'])

    '''
    Summary: Check that get_request_status_code == 200 and message == "no messages" and
             get_request_status_reason == 'Ok'

    Precondition: The selected queue contains no messages

    Steps:
        1. Set value to url (e.g. "http://localhost:8888")

        2. Set value to queue (e.g. 1)

        3. Run get-request GetRequest.get(queue)

    Expected result: GET request has status code == 200, text == "no messages", reason == "Ok"

    '''

    assert (get_request_status_code == 200 and message == "no messages" and get_request_status_reason == 'Ok')

#******************************************************************************************************************


def test_post_to_empty_numbered_queue():
    url = "http://localhost:8888"
    queue = 2
    number_of_messages = 1
    # operations_with_numbers = list(range(1, number_of_messages + 1))
    # messages = []
    # for num in operations_with_numbers:
    #     messages.append("text_" + str(num))
    messages = creating_list_of_messages(number_of_messages)

    PostRequest = Client(url)
    messages_from_client_stored_to_queue = []
    post_request_status_code = 0
    post_request_reason = 0
    for i in range(0, number_of_messages):
        message_from_client = messages[i]
        post_request_result = PostRequest.post(queue, message_from_client)
        post_request_status_code = post_request_result.status_code
        post_request_reason = post_request_result.reason
        if post_request_result.status_code == 201:
            messages_from_client_stored_to_queue.append(message_from_client)

    messages_returned_by_get = []
    GetRequest = Client(url)
    for i in range(1, number_of_messages + 1):
        get_request_result = GetRequest.get(queue)
        if get_request_result.status_code == 200:
            messages_returned_by_get.append(json.loads(get_request_result.text)['message'])

    '''
    Summary: Check that post request successfully receives message from the client and saves it in a numbered
             queue.

    Precondition: The selected queue contains no messages

    Steps:
        1. Set value to url (e.g. "http://localhost:8888")

        2. Set value to queue (e.g. 2)

        3. Run post-request PostRequest.post(queue, "text_1")

        4. Run get-request with GetRequest.get(queue)

    Expected result:  Post request has  status_code == 201, reason == 'Ok' and the message received from
                      the client and saved in a numbered queue by post request matches the message received by get
                      request to this queue.
    '''

    assert (post_request_status_code == 201 and post_request_reason == 'Ok' and
            messages_from_client_stored_to_queue == messages_returned_by_get)

#********************************************************************************************************************


def test_put_oldest_message_in_numbered_queue():
    url = "http://localhost:8888"
    queue = 3
    new_message = "text_changed"

    number_of_messages = 2
    # operations_with_numbers = list(range(1, number_of_messages + 1))
    # messages = []
    # for num in operations_with_numbers:
    #     messages.append("text_" + str(num))
    messages = creating_list_of_messages(number_of_messages)

    messages_from_client_stored_to_queue = []
    PostRequest = Client(url)
    for i in range(0, number_of_messages):
        message_from_client = messages[i]
        post_request_result = PostRequest.post(queue, message_from_client)
        if post_request_result.status_code == 201:
            messages_from_client_stored_to_queue.append(message_from_client)

    new_message = "text_changed"
    message_transmitted_by_put_request = ""
    PutRequest = Client(url)
    put_request_result = PutRequest.put(queue, new_message)
    put_request_status_code = put_request_result.status_code
    put_request_reason = put_request_result.reason
    if put_request_result.status_code == 201:
        message_transmitted_by_put_request = new_message

    message_returned_by_get = []
    GetRequest = Client(url)
    get_request_result = GetRequest.get(queue)
    if get_request_result.status_code == 200:
        message_returned_by_get.append(json.loads(get_request_result.text)['message'])

    '''
    Summary: Check that put request successfully changes oldest message in a numbered 
             queue.

    Precondition: The selected queue contains no messages

    Steps:
        1. Set value to url (e.g. "http://localhost:8888")

        2. Set value to queue (e.g. 3)

        3. Run post-request PostRequest.post(queue, "text_1")

        4. Run post-request PostRequest.post(queue, "text_2")

        5. Run put-request PutRequest.get(queue, new_message)
        
        6. Run get-request with GetRequest.get(queue)


    Expected result:  GET request to the selected queue has status_code == 201, reason == "Ok", text == "text_changed" 
    '''

    assert (messages_from_client_stored_to_queue == ["text_1", "text_2"] and
            put_request_reason == "Ok" and put_request_status_code == 201 and
            message_transmitted_by_put_request == message_returned_by_get)

#***********************************************************************************************************************


def test_get_oldest_message_from_numbered_queue():
    url = "http://localhost:8888"
    queue = 4
    number_of_messages = 2
    # operations_with_numbers = list(range(1, number_of_messages + 1))
    # messages = []
    # for num in operations_with_numbers:
    #     messages.append("text_" + str(num))
    messages = creating_list_of_messages(number_of_messages)

    messages_from_client_stored_to_queue = []
    PostRequest = Client(url)
    for i in range(0, number_of_messages):
        message_from_client = messages[i]
        post_request_result = PostRequest.post(queue, message_from_client)
        if post_request_result.status_code == 201:
            messages_from_client_stored_to_queue.append(message_from_client)

    oldest_message_returned_by_get = ""
    GetRequest = Client(url)
    get_request_result = GetRequest.get(queue)
    if get_request_result.status_code == 200:
        oldest_message_returned_by_get = json.loads(get_request_result.text)['message']

    '''
    Summary: Check that GET request returns oldest message from the numbered queue

    Precondition: The selected queue contains no messages

     Steps:

     1.   Set value to url (e.g. "http://localhost:8888")

     2. Set value to queue (e.g. 4)

     3. Run post-request PostRequest.post(queue, "text_1")

     4. Run post-request PostRequest.post(queue, "text_2")

     5. Run get-request GetRequest.get(queue)

    Expected result: GET request returns oldest message from the numbered queue text == "text_1"

    '''
    assert (messages_from_client_stored_to_queue == ["text_1", "text_2"] and
            oldest_message_returned_by_get == "text_1")

# *******************************************************************************************************************

def test_delete_from_numbered_queue():
    url = "http://localhost:8888"
    queue = 5
    number_of_messages = 2
    # operations_with_numbers = list(range(1, number_of_messages + 1))
    # messages = []
    # for num in operations_with_numbers:
    #     messages.append("text_" + str(num))
    messages = creating_list_of_messages(number_of_messages)

    messages_from_client_stored_to_queue = []
    PostRequest = Client(url)
    for i in range(0, number_of_messages):
        message_from_client = messages[i]
        post_request_result = PostRequest.post(queue, message_from_client)
        if post_request_result.status_code == 201:
            messages_from_client_stored_to_queue.append(message_from_client)

    DeleteRequest = Client(url)
    delete_request_result = DeleteRequest.get(queue)
    delete_request_status_code = delete_request_result.status_code
    delete_request_reason = delete_request_result.reason

    oldest_message_returned_by_get = ""
    GetRequest = Client(url)
    get_request_result = GetRequest.get(queue)
    if get_request_result.status_code == 200:
        oldest_message_returned_by_get = json.loads(get_request_result.text)['message']

    '''
    Summary: Check that DELETE request deletes oldest message from the numbered queue

    Precondition: The selected queue contains no messages

     Steps:

         1.   Set value to url (e.g. "http://localhost:8888")

         2. Set value to queue (e.g. 5)

         3. Run post-request PostRequest.post(queue, "text_1")

         4. Run post-request PostRequest.post(queue, "text_2")

         5. Run delete-request GetRequest.get(queue)

         6. Run get-request GetRequest.get(queue)

    Expected result: DELETE request has status_code == 200, reason == "Ok" and oldest message returned by GET request
             to this queue == "text_2"
    '''
    assert (delete_request_status_code == 200 and delete_request_reason == "Ok" and oldest_message_returned_by_get ==
            "text_2")


#**********************************************************************************************************************


def test_oldest_message_was_deleted_after_get_request_to_numbered_queue():
    url = "http://localhost:8888"
    queue = 10000
    number_of_messages = 2
    # operations_with_numbers = list(range(1, number_of_messages + 1))
    # messages = []
    # for num in operations_with_numbers:
    #     messages.append("text_" + str(num))
    messages = creating_list_of_messages(number_of_messages)

    messages_from_client_stored_to_queue = []
    PostRequest = Client(url)
    for i in range(0, number_of_messages):
        message_from_client = messages[i]
        post_request_result = PostRequest.post(queue, message_from_client)
        if post_request_result.status_code == 201:
            messages_from_client_stored_to_queue.append(message_from_client)

    oldest_message_returned_by_first_get_request = ""
    GetRequest = Client(url)
    get_request_result = GetRequest.get(queue)
    if get_request_result.status_code == 200:
        oldest_message_returned_by_first_get_request = json.loads(get_request_result.text)['message']

    oldest_message_returned_by_second_get_request = ""
    GetRequest = Client(url)
    get_request_result = GetRequest.get(queue)
    if get_request_result.status_code == 200:
        oldest_message_returned_by_second_get_request = json.loads(get_request_result.text)['message']

    '''
        Summary: Check that oldest message was deleted after GET request to the numbered queue

        Precondition: The selected queue contains no messages

        Steps:
            1. Set value to url (e.g. "http://localhost:8888")

            2. Set value to queue_number (e.g. 10000)

            3. Run post-request PostRequest.post(queue, "text_1")

            4. Run post-request PostRequest.post(queue, "text_2")

            5. Run get-request GetRequest.get(queue)

            6. Run get-request GetRequest.get(queue)

        Expected result: Second GET request to the same queue returns message "text_2"

        '''
    assert (messages_from_client_stored_to_queue == ["text_1", "text_2"] and
            oldest_message_returned_by_first_get_request == "text_1" and
            oldest_message_returned_by_second_get_request == "text_2")
