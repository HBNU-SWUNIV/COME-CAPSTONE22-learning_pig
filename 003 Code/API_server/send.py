from flask import Flask, json
import requests

app = Flask(__name__)

ID = [1, 2, 3, 4, 5, 1, 1, 2, 2]
distance = [1.1, 1.2, 1.5, 2.1, 2.2, 2.6, 2.5, 3.8, 4.2]


def send():
    url = "http://1.226.102.182:7070/input"
    data = {
        'id': ID,
        'distance': distance}

    data = json.dumps(data)

    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    response = requests.post(url, data, headers=headers)
    print(response)
    return response.text


if __name__ == "__main__":
    send()
