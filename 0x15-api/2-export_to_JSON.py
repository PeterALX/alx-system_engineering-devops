#!/usr/bin/python3
""" get user's todo info from an api and store it in json"""

if __name__ == '__main__':
    import json
    import requests
    import sys

    userId = sys.argv[1]
    todosUrl = f'https://jsonplaceholder.typicode.com/todos?userId={userId}'
    userUrl = f'https://jsonplaceholder.typicode.com/users?id={userId}'
    userTasks = requests.get(todosUrl).json()
    employee = requests.get(userUrl).json()[0]

    data = {userId: []}
    for task in userTasks:
        t = {'task': task.get('title'), 'completed': task.get('completed'), 'username': employee.get('username')}
        data[userId].append(t)
    print(data)
    with open(f'{userId}.json', 'w', encoding='UTF8') as f:
       json.dump(data, f) 
