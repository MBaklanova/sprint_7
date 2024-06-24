class Url:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    CREATE_COURIER_HANDLE = '/api/v1/courier'
    LOGIN_COURIER_HANDLE = '/api/v1/courier/login'
    ORDERS_HANDLE = '/api/v1/orders'
    ORDERS_ACCEPT_HANDLE = '/api/v1/orders/accept'
    ORDERS_NUMBER_HANDLE = '/api/v1/orders/track'


class Messages:
    CONFLICT_409 = 'Этот логин уже используется. Попробуйте другой.'
    CREATE_BAD_REQUEST_400 = 'Недостаточно данных для создания учетной записи'
    LOGIN_BAD_REQUEST_400 = 'Недостаточно данных для входа'
    LOGIN_NOT_FOUND_404 = 'Учетная запись не найдена'
    DELETING_COURIER_400 = 'Недостаточно данных для удаления курьера'
    DELETING_COURIER_404 = 'Курьера с таким id нет.'
    ACCEPTING_ORDER_400 = 'Недостаточно данных для поиска'
    ACCEPTING_ORDER_NO_COURIER_ID_404 = 'Курьера с таким id не существует'
    ACCEPTING_ORDER_NO_ORDER_ID_404 = 'Заказа с таким id не существует'
    GER_ORDER_BY_NUMBER_400 = 'Недостаточно данных для поиска'
    GET_ORDER_BY_NUMBER_404 = 'Заказ не найден'


class OrderTestData:
    SCOOTER_COLORS = ['[]', '["BLACK"]', '["GREY"]', '["BLACK", "GREY"]']
    ORDER = {
            "firstName": "Mari",
            "lastName": "Pavlova",
            "address": "Gagarina, 8",
            "metroStation": 4,
            "phone": "+7 800 100 22 33",
            "rentTime": 5,
            "deliveryDate": "2024-07-06",
            "comment": "Privet. V dver' stuchat'",
            "color": []
            }