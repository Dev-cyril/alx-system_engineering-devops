#!/usr/bin/python3

"""A module that, using this REST API, for a given employee ID,
returns information about his/her Todo list progress."""

import requests
import sys

if __name__ == '__main__':
    """prints the information about an API"""
    userData = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                            format(sys.argv[1])).json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos/',
                        params={"userId": sys.argv[1]}).json()
    completed = [t.get("title") for t in todo if t.get("completed") is True]
    for k in todo:
        if (int(sys.argv[1]) == userData['id']) and \
                (userData['id'] == k['userId']):
            print('Employee {} is done with tasks({}/{}):'
                  .format(userData['name'], len(completed), len(todo)))
            for j in completed:
                print('\t {}'.format(j))
        break
