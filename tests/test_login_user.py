import allure
import requests

from data.handlers import Handlers
from data.urls import Urls
from data.user_data import User


class TestLogin:

    @allure.title('Логин под существующим пользователем')
    def test_login_user(self):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.LOGIN}', data=User.data_correct)
        assert response.status_code == 200 and response.json().get('success') is True

    @allure.title('Логин с некорректным логином/паролем')
    def test_login_user_error(self):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.LOGIN}', data=User.data_negative)
        assert response.status_code == 401 and response.json().get('success') is False
