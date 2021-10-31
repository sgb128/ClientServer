""" Unit-тесты клиента """

import unittest

from lesson4.common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, \
    RESPONSE, ERROR, DEFAULT_PORT, PORT
from lesson4.client import create_presence, check_answer


class TestClient(unittest.TestCase):
    """
    Класс с тестами client-а
    """

    def test_create_presence(self):
        """ Тест корректного запроса о присутствии клиента """
        test = create_presence()
        test[TIME] = 1.1  # возьму из примера, зачем усложнять ;-)
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, PORT: DEFAULT_PORT, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_incorrect_create_presence(self):
        """ Тест некорректного запроса о присутствии клиента """
        test = create_presence()
        test[TIME] = 1.1
        self.assertNotEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_create_presence_port(self):
        """ Тест указания порта в запросе о присутствии клиента """
        test = create_presence()
        test[TIME] = 1.1
        self.assertIn(PORT, test)

    def test_create_presence_port_value(self):
        """ Тест значения порта в запросе о присутствии клиента """
        test = create_presence()
        test[TIME] = 1.1
        self.assertEqual(test[PORT], DEFAULT_PORT)

    def test_check_answer_200(self):
        """ Тест корректного разбора ответа от сервера (200) """
        self.assertEqual(check_answer({RESPONSE: 200}), '200 : OK')

    def test_incorrect_check_answer_200(self):
        """ Тест некорректного разбора ответа от сервера (200) """
        self.assertNotEqual(check_answer({RESPONSE: 200}), '400 : Bad Request')

    def test_check_answer_400(self):
        """ Тест корректного разбора (400) """
        self.assertEqual(check_answer({RESPONSE: 400, ERROR: 'Bad Request'}), '400 : Bad Request')

    def test_incorrect_check_answer_400(self):
        """ Тест некорректного разбора (400) """
        self.assertNotEqual(check_answer({RESPONSE: 400, ERROR: 'Bad Request'}), '200 : OK')

    def test_no_answer(self):
        """ Тест исключения без поля RESPONSE """
        self.assertRaises(ValueError, check_answer, {ERROR: 'Bad Request'})


if __name__ == '__main__':
    unittest.main()