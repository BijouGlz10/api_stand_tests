import configuration
import requests
import data

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)
response = get_docs()


def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH, params={"count": 20})
response = get_logs()

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
response = get_users_table()


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, "https://cnt-9dee143e-6c48-4e55-8581-f96a8566224c.containerhub.tripleten-services.com", json = { "firstName": "Andrea", "phone": "+11234567890", "address": "123 Elm Street, Hilltop" }, headers = {"Content-Type": "application/json"}) # inserta los encabezados

response = post_new_user(data.user_body)


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

response = post_new_user(data.user_body);


