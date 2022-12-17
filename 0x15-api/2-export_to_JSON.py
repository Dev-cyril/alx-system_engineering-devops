#!/usr/bin/python3

"""A module that exports data from an API to a JSON file."""

import json
import requests
import sys


if __name__ == '__main__':
    """dumps a dictionary and write into a json file"""

    userData = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(sys.argv[1])).json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos/',
                        params={"userId": sys.argv[1]}).json()

    dic = {sys.argv[1]: [
        {'task': t['title'], 'completed': t['completed'],
            'username': userData['username']} for t in todo]
    }
    obj = json.dumps(dic)
    with open('{}.json'.format(sys.argv[1]), "w") as file:
        file.write(obj)
