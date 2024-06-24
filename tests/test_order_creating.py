import allure
import pytest
from conftest import *
import helpers
from data import OrderTestData


@allure.story('Тесты создания заказа')
class TestOrderCreating:
    @allure.title('Тест успешного создания заказа')
    @pytest.mark.parametrize('color', OrderTestData.SCOOTER_COLORS)
    def test_successful_order_creating(self, color):
        response = helpers.order_create(color)
        assert 'track' in response.text