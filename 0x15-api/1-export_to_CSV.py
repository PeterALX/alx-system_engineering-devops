#!/usr/bin/python3
""" get user's todo info from an api and store it in csv """

if __name__ == '__main__':
    import requests
    import sys

    import requests
    import sys

    userId = sys.argv[1]
    todosUrl = f'https://jsonplaceholder.typicode.com/todos?userId={userId}'
    userUrl = f'https://jsonplaceholder.typicode.com/users?id={userId}'
    userTasks = requests.get(todosUrl).json()
    employee = requests.get(userUrl).json()[0]

    data = ""
    for task in userTasks:
        data = data + '"{}","{}","{}","{}"\n'.\
                format(userId, employee.get('username'),
                       task.get('completed'), task.get('title'))
    with open(f'{userId}.csv', 'w', encoding='UTF8') as myFile:
        myFile.write(data)
