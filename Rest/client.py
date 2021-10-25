import requests

url = 'http://localhost:8888'
key_mess = 'message'
value_mess = 'sent_2'
key_queue = 'queue'
value_queue = 1


#result = requests.get(url)
result = requests.get('http://localhost:8888').text
print(result)

#result = requests.post('http://localhost:8888')
#print(result.status_code)

#result = requests.put('http://localhost:8888', json={'message': 'this message was update by put request'})
#print(result.status_code)

#print(requests.delete('http://localhost:8888').status_code)


