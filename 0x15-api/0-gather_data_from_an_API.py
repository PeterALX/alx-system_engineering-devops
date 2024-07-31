#!/usr/bin/python3
""" display todo info for a user from an api"""

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
    userTasksDone = [task for task in userTasks if task.get('completed')]

    print('Employee {} is done with tasks({}/{}):'.
          format(employee.get("name"), len(userTasksDone), len(userTasks)))
    for task in userTasksDone:
        print(f'\t {task.get("title")}')
