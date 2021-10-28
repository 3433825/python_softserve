import requests

#result = requests.get(url)

result = requests.get('http://localhost:8888').text
print(result)

#result = requests.post('http://localhost:8888')
#print(result.status_code)

#result = requests.put('http://localhost:8888', json={'message': 'this message was update by put request'})
#print(result.status_code)

#print(requests.delete('http://localhost:8888').status_code)


