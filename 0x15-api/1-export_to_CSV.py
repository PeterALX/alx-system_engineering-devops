#!/usr/bin/python3
""" get user's todo info from an api and store it in csv """

if __name__ == '__main__':
    import requests
    import sys

    userId = sys.argv[1]
    todosUrl = 'https://jsonplaceholder.typicode.com/todos/'
    userUrl = f'https://jsonplaceholder.typicode.com/users/{userId}'
    tasks = requests.get(todosUrl).json()
    employee = requests.get(userUrl).json()
    userTasks = [task for task in tasks
                 if task.get('userId') == employee.get('id')]

    data = ""
    for task in userTasks:
        data = data + '"{}","{}","{}","{}"\n'.\
                format(userId, employee.get('name'),
                       task.get('completed'), task.get('title'))
    with open(f'{userId}.csv', 'w', encoding='UTF8') as myFile:
        myFile.write(data)
