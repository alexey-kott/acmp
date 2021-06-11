import sys

import requests


host = sys.stdin.readline().strip()
port = sys.stdin.readline().strip()
a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

# host = 'http://0.0.0.0'
# port = 8080
# a = b = 0

url = f"{host}:{port}?a={a}&b={b}"
response = requests.get(url)
numbers = response.json()

print(sum(numbers))
