from requests import get, put

put('http://127.0.0.1:8080/todo1', data={'data': 'Remember the milk'}).json()
print(get('http://127.0.0.1:8080/todo1').json())

put('http://127.0.0.1:8080/todo2', data={'data': 'Change my brakepads'}).json()
print(get('http://127.0.0.1:8080/todo2').json())
