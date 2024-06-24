import allure
import requests


from data import Url


@allure.story('Тесты списков заказов')
class TestOrderList:
    @allure.title('Тест успешного получения списка заказа')
    def test_successful_get_order_list(self):
        response = requests.get(Url.BASE_URL+Url.ORDERS_HANDLE)
        assert 'orders' in response.text