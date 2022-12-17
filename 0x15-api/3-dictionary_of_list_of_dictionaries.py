#!usr/bin/python3

"""A module that exports data from an API to a JSON file."""

import json
import requests


if __name__ == '__main__':
    """dumps a dictionary and write into a json file"""

    userData = requests.get(
        'https://jsonplaceholder.typicode.com/users/').json()

    dic = {
        u['id']: [
                    {'task': t['title'],
                        'completed': t['completed'],
                        'username': u['username']}
                    for t in requests.get(
                        'https://jsonplaceholder.typicode.com/todos/',
                        params={"userId": u['id']}).json()]
        for u in userData
    }
    with open('todo_all_employees.json', "w") as file:
        json.dump(dic, file)
