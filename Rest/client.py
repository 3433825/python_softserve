import requests


class Task_rest():

    def __init__(self, url):
        self.url = url

    def get(self, queue):
        get_request = requests.get(self.url, params={'queue': queue})
        return get_request

    def post(self, queue, message):
        post_request = requests.post(self.url, json={'message': message, 'queue': queue})
        return post_request

    def delete(self, queue):
        delete_request = requests.delete(self.url, params={'queue': queue})
        return delete_request

    def put(self, queue, message):
        put_request = requests.put(self.url, json={'message': message, 'queue': queue})
        return put_request

