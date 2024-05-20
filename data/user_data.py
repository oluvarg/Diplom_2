from faker import Faker


class User:

    data_correct = {
        "email": 'ou_test_1305@ya.ru',
        "password": "password"}

    data_negative = {
        "email": '1305_ou_test_1305@yandex.ru',
        "password": "password"}

    data_double = {
        "email": 'ou_test_1305@ya.ru',
        "password": "password",
        "name": "username"}

    data_without_email = {
        "email": '',
        "password": "password",
        "name": "username"}

    data_without_password = {
        "email": 'ou_test_1305@ya.ru',
        "password": "",
        "name": "username"}

    data_without_name = {
        "email": 'ou_test_1305@ya.ru',
        "password": "password",
        "name": ""}

    data_updated = {
        "email": 'ou_test_1305@ya.ru',
        "password": "password",
        "name": "test"}
