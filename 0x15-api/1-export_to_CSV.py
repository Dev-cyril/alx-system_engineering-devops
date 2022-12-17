#!/usr/bin/python3

"""A module that exports data from an API to a CSV file."""

import csv
import requests
import sys


if __name__ == '__main__':
    """exports  a dictionary to a csv file"""

    userData = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                            format(sys.argv[1])).json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos/',
                        params={"userId": sys.argv[1]}).json()

    with open('{}.csv'.format(sys.argv[1]), "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [sys.argv[1], userData['username'],
                t.get("completed"), t.get("title")]
         ) for t in todo]
