import allure
import helpers
from data import Messages
from conftest import *

@allure.story('Тесты на вход курьера')
class TestCourierLogin:
    @allure.title('Проверка успешного логина курьера. Получаем статус 200 и id курьера')
    def test_successful_courier_login(self, courier):
        response = helpers.courier_login(courier['login'], courier['password'])
        assert response.status_code == 200 and 'id' in response.text, \
            f'Status code: {response.status_code}, Response: {response.text}'

    @allure.title('Проверка, что если не передано поле логина, запрос возвращает ошибку 400')
    def test_courier_login_with_empty_login(self, courier):
        response = helpers.courier_login('', courier['password'])
        assert response.status_code == 400 and response.json()['message'] == Messages.LOGIN_BAD_REQUEST_400, \
            f"Status code: {response.status_code}, Response message: {response.json()}"

    @allure.title('Проверка, что если не передано поле пароля, запрос возвращает ошибку 400')
    def test_courier_login_with_empty_password(self, courier):
        response = helpers.courier_login(courier['login'], '')
        assert response.status_code == 400 and response.json()['message'] == Messages.LOGIN_BAD_REQUEST_400, \
            f"Status code: {response.status_code}, Response message: {response.json()}"

    @allure.title('Проверка невозможности авторизоваться с несуществующим логином. Получаем ошибку 404')
    def test_courier_login_with_incorrect_login(self, courier):
        response = helpers.courier_login(courier['password'], courier['password'])
        assert response.status_code == 404 and response.json()['message'] == Messages.LOGIN_NOT_FOUND_404, \
            f"Status code: {response.status_code}, Response message: {response.json()}"

    @allure.title('Проверка невозможности авторизоваться с несуществующим паролем. Получаем ошибку 404')
    def test_courier_login_with_incorrect_password(self, courier):
        response = helpers.courier_login(courier['login'], courier['login'])
        assert response.status_code == 404 and response.json()['message'] == Messages.LOGIN_NOT_FOUND_404, \
            f"Status code: {response.status_code}, Response message: {response.json()}"