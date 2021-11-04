import requests

class Task_rest():

    def __init__(self, url, parameter_for_query):
        self.url = url
        self.parameter_for_query = parameter_for_query

    def get(self):
        query_get = requests.get(self.url, params=self.parameter_for_query)
        return query_get

    def delete(self, ):
        query_delete = requests.delete(self.url, params=self.parameter_for_query)
        return query_delete

    def post(self):
        query_post = requests.post(self.url, json=self.parameter_for_query)
        return query_post

    def put(self):
        query_put = requests.put(self.url, params=self.parameter_for_query)
        return query_put

def message_text_from_response(message):
    message_from_response_split = message.split(':')
    message_from_response_all_string = message_from_response_split[1]
    message_from_response_clear_left = message_from_response_all_string.lstrip(' "')
    text_from_response = message_from_response_clear_left.rstrip('"}')
    return text_from_response

