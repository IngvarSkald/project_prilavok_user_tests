import requests
import config
import data

def create_new_user():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=data.user_body)
