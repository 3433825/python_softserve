import pytest
import requests

@pytest.mark.parametrize("text_mess,expected", [('text_0', 201)])
def test_post_request(text_mess, expected):
    ''' Check-list for Rest:
    Method POST
    1. Check that client can successfully store first valid message:
       1.1. without queue number.
       1.2. with queue number = 0.
       1.3. with queue number out of order (e.g. queue number = 10000).
    2. Check that client can successfully store next valid message:
       2.1. without queue number after message with queue number = 0
       2.2. with queue number in order(e.g. queue number  = 1 after first message with queue number = 0)
       2.3. with queue number out of order ( e.g. with queue number = 100 after first message
            with queue number = 10000 )
    Method GET
    3. Check that client can successfully retrieve message without queue in request when queue has only one message
    4. Check that client can successfully retrieve message without queue in request when queue has several messages
    5. Check that client can successfully retrieve message when queue in request  has value
       5.1. when last message has queue in order (e.g. first message queue = 0 and second message queue = 1)
       5.2. when last message has queue out of order (e.g. first message queue = 10000 and
            second message queue = 100)
    Method Put
    Method DELETE

    Positive test-cases for post request:
    Rest-1.1. Check that client can store first valid message to server with default queue alias
    Precondition:
    1. server.py is running
    2. import pytest
    3. import requests
    Steps:
    run request - post('http://localhost:8888', json={'message': text_0}).status_code
    Expected result:
    status_code = 201
    '''

    result = requests.post('http://localhost:8888', json={'message': text_mess})
#   assert result.status_code == expected
    pass

@pytest.mark.parametrize("text_mess,queue_num, expected", [('text_1', 1, 201)])
def test_post_request(text_mess, queue_num, expected):

    '''Positive test-cases for post request:

    Rest-1.2. Check that client can store first valid message to server with queue alias
    Precondition:
    1. server.py is running
    2. import pytest
    3. import requests
    4. Value of variables
       text_mess = 'text_0'
       queue_num = 0

    Steps:
    run request - post('http://localhost:8888', json={'message': text_mess, 'queue': queue_num}).status_code
    Expected result:
    status_code = 201
    '''

    result = requests.post('http://localhost:8888', json={'message': text_mess, 'queue': queue_num})
    assert result.status_code == expected
#    pass

@pytest.mark.parametrize("text_mess, queue_num, expected", [('text_100', 100,  201)])
def test_post_request(text_mess, queue_num, expected):
    '''Positive test-cases for post request:

    Rest-1.3.Check that client can successfully store first valid message with queue number out of order
    (e.g. queue number = 10000).

    Precondition:
    1. server.py is running
    2. import pytest
    3. import requests
    4. Value of variables
       text_mess = 'text_10000'
       queue_num = 10000

    Steps:
    run request - post('http://localhost:8888', json={'message': text_mess, 'queue': queue_num}).status_code
    Expected result:
    status_code = 201
    '''

#   result = requests.post('http://localhost:8888', json={'message': text_mess,'queue': queue_num})
#   assert result.status_code == expected
    pass


@pytest.mark.parametrize("text_mess, expected", [('text_100', 201)])
def test_post_request(text_mess, expected):
    '''Positive test-cases for post request:

    Rest-2.1. Check that client can successfully store next valid message without queue number after message
    with queue number = 0

    Precondition:
    1. server.py is running
    2. import pytest
    3. import requests
    4. message 'text_0' with queue number = 0 stored to the localhost
    4. Value of variables
       text_mess = 'text_1'

    Steps:
    run request - post('http://localhost:8888', json={'message': text_mess}).status_code
    Expected result:
    status_code = 201
    '''
    result = requests.post('http://localhost:8888', json={'message': text_mess})
    #   assert result.status_code == expected
    pass

@pytest.mark.parametrize("text_mess, queue_num, expected", [('text_1', 1,  201)])
def test_post_request(text_mess, queue_num, expected):
    '''Positive test-cases for post request:

    Rest-2.2. Check that client can successfully store next valid message with queue number in order
            (e.g. queue number  = 1 after first message with queue number = 0)

    Precondition:
    1. server.py is running
    2. import pytest
    3. import requests
    4. first message with text = 'text_0' and queue = 0 is stored to localhost
    4. Value of variables
       text_mess = 'text_1'
       queue_num = 1

    Steps:
    run request - post('http://localhost:8888', json={'message': text_mess, 'queue': queue_num}).status_code
    Expected result:
    status_code = 201
    '''
    result = requests.post('http://localhost:8888', json={'message': text_mess,'queue': queue_num})
#   assert result.status_code == expected
    pass

@pytest.mark.parametrize("text_mess, queue_num, expected", [('text_1', 1,  201)])
def test_post_request(text_mess, queue_num, expected):
    '''Positive test-cases for post request:

    Rest-2.3.Check that client can successfully store next valid message with queue number out of order
           ( e.g. with queue number = 100 after first message with queue number = 10000 )

    Precondition:
    1. server.py is running
    2. import pytest
    3. import requests
    4. first message with text = 'text_10000' and queue = 10000 is stored to localhost
    4. Value of variables
       text_mess = 'text_100'
       queue_num = 100

    Steps:
    run request - post('http://localhost:8888', json={'message': text_mess, 'queue': queue_num}).status_code
    Expected result:
    status_code = 201
    '''

    result = requests.post('http://localhost:8888', json={'message': text_mess,'queue': queue_num})
#   assert result.status_code == expected
    pass

@pytest.mark.parametrize("text_mess, queue_num, expected", [('text_1', 1,  201)])
def test_post_request(text_mess, queue_num, expected):
    '''Positive test-cases for post request:

    Rest-3 Check that client can successfully store next valid message with queue number out of order
           ( e.g. with queue number = 100 after first message with queue number = 10000 )

    Precondition:
    1. server.py is running
    2. import pytest
    3. import requests
    4. first message with text = 'text_10000' and queue = 10000 is stored to localhost
    4. Value of variables
       text_mess = 'text_100'
       queue_num = 100

    Steps:
    run request - post('http://localhost:8888', json={'message': text_mess, 'queue': queue_num}).status_code
    Expected result:
    status_code = 201
    '''

    result = requests.post('http://localhost:8888', json={'message': text_mess,'queue': queue_num})
#   assert result.status_code == expected
    pass



