import pytest
import allure
import requests

from data.handlers import Handlers
from data.urls import Urls
from data.user_data import User
from helpers import Helper


class TestCreateUser:

    @allure.title('Создание уникального пользователя')
    def test_create_new_user_success(self):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_USER}', data=Helper.create_data_user())
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title('Создание пользователя, который уже зарегистрирован')
    def test_create_double_user_error(self):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_USER}', data=User.data_double)
        assert response.status_code == 403 and 'User already exists' in response.text

    @allure.title('Создание пользователя с некорректными данными/с незаполненными обязательными полями')
    @pytest.mark.parametrize("user_data", [User.data_without_email, User.data_without_password, User.data_without_name])
    def test_create_user_incorrect_data(self, user_data):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_USER}', data=user_data)
        assert response.status_code == 403 and 'Email, password and name are required fields' in response.text
