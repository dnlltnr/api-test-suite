
import requests


def create_user(base_url, payload):

    response = requests.post(base_url, json=payload, timeout=3)
    data = response.json()
    return response, data


def get_users(base_url):

    response = requests.get(base_url, timeout=3)
    data = response.json()
    return response, data
