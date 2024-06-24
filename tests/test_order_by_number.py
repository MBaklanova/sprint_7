import allure
import requests
import helpers
from conftest import *
from data import Url, Messages


@allure.story('Тесты получения заказов по номеру')
class TestOrderByNumber:
    @allure.title('Успешное получение заказа по его номеру. Получаем код 200 и данные с заказом')
    def test_get_order_by_number(self):
        order_number = helpers.get_orders_numbers()[0]
        response = requests.get(f'{Url.BASE_URL}{Url.ORDERS_NUMBER_HANDLE}?t={order_number}')
        assert response.status_code == 200 and 'order' in response.text, \
            f'Status code: {response.status_code}, Response text: {response.text}'

    @allure.title('Проверка невозможности получить заказ, если не отправить его номер. '
                        'Получаем код 400 и сообщение: Недостаточно данных для поиска')
    def test_get_order_with_no_number(self):
        response = requests.get(f'{Url.BASE_URL}{Url.ORDERS_NUMBER_HANDLE}?t=')
        assert response.status_code == 400 and response.json()['message'] == Messages.GER_ORDER_BY_NUMBER_400, \
            f'Status code: {response.status_code}, Response message: {response.json()['message']}'

    @allure.title('Проверка невозможности получить заказ, если отправить несуществующий номер. '
                        'Получаем код 404 и сообщение: Заказ не найден')
    def test_get_order_with_incorrect_number(self):
        response = requests.get(f'{Url.BASE_URL}{Url.ORDERS_NUMBER_HANDLE}?t=0')
        assert response.status_code == 404 and response.json()['message'] == Messages.GET_ORDER_BY_NUMBER_404, \
            f'Status code: {response.status_code}, Response message: {response.json()['message']}'