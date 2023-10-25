import sender_stand_request
import data
import config
import requests


# Изменение тела запроса
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


# Получение токена
def get_new_user_token():
    return requests.post(config.URL_SERVICE + config.CREATE_USER_PATH,
                         json=data.user_body,
                         headers=data.headers)


response_token = get_new_user_token()
data.auth_token["Authorization"] = "Bearer " + response_token.json()["authToken"]


# Позитивная проверка
def positive_assert(name):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body, data.auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == name


# Негативная проверка
def negative_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, data.auth_token)
    assert response.status_code == 400


# Тест 1. Успешное создание набора. Параметр name состоит из 1 символа
def test_create_kit_body_1_letter_in_name_get_success_response():
    positive_assert("a")


# Тест 2. Успешное создание набора. Параметр name состоит из 511 символов
def test_create_kit_body_511_letter_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


# Тест 3. Ошибка. В параметре name 0 символов
def test_create_kit_body_0_letter_in_name_get_fail_response():
    kit_body = get_kit_body("")
    negative_assert(kit_body)


# Тест 4. Ошибка. В параметре name символов больше допустимого(512)
def test_create_kit_body_512_letter_in_name_get_fail_response():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert(kit_body)


# Тест 5. Успешное создание набора. Параметр name состоит из английских букв
def test_create_kit_body_english_letters_in_name_get_success_response():
    positive_assert("QWErty")


# Тест 6. Успешное создание набора. Параметр name состоит из русских букв
def test_create_kit_body_russian_letters_in_name_get_success_response():
    positive_assert("Мария")


# Тест 7. Успешное создание набора. Параметр name состоит из спецсимволов("%@$")
def test_create_kit_body_special_in_name_get_success_response():
    positive_assert("%@$")


# Тест 8. Успешное создание набора. Параметр name включает пробелы ("Человек и КО")
def test_create_kit_body_space_in_name_get_success_response():
    positive_assert("Человек и КО")


# Тест 9. Успешное создание набора. Параметр name включает цифры ("123")
def test_create_kit_body_numbers_in_name_get_success_response():
    positive_assert("123")


# Тест 10. Ошибка. Параметр name не передан
def test_create_kit_body_null_in_name_get_fail_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert(kit_body)


# Тест 11. Ошибка. Передан другой тип параметра name (123)
def test_create_kit_body_int_in_name_get_fail_response():
    kit_body = get_kit_body(123)
    negative_assert(kit_body)
