#!/usr/bin/python3
""" display todo info for a user from an api"""

if __name__ == '__main__':
    import requests
    import sys

    userId = sys.argv[1]
    todosUrl = f'https://jsonplaceholder.typicode.com/todos?userId={userId}'
    userUrl = f'https://jsonplaceholder.typicode.com/users?id={userId}'
    userTasks = requests.get(todosUrl).json()
    employee = requests.get(userUrl).json()[0]
    userTasksDone = [task for task in userTasks if task.get('completed')]

    print('Employee {} is done with tasks({}/{}):'.
          format(employee.get("name"), len(userTasksDone), len(userTasks)))
    for task in userTasksDone:
        print(f'\t {task.get("title")}')
