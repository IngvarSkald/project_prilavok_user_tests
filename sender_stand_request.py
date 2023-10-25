import config
import requests
import data


def post_new_user(body):
    return requests.post(config.URL_SERVICE + config.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())


def post_new_client_kit(kit_body, auth_token):
    return requests.post(config.URL_SERVICE + config.CREATE_KIT_PATH,
                         json=kit_body,
                         headers=auth_token)


response = post_new_client_kit(data.kit_body, data.auth_token)
print(response.status_code)
print(response.json())
