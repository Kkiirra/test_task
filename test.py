import requests
import unittest
from validation import validate_date, validate_currencies, validate_base_currency, validate_amount


class TestExchangeFunctions(unittest.TestCase):
    def test_exchange_currency_request(self):
        expected_response = [
            {'currency': 'EUR', 'amount': '41.5205064'},
            {'currency': 'GBP', 'amount': '35.7403134'}
        ]

        data = {
            "input_currency": "USD",
            "output_currencies": ['EUR', 'GBP'],
            "amount": 50.46,
            "date": "2021-02-23"
        }

        response = requests.post('http://127.0.0.1:8000/exchange/', json=data)

        self.assertEqual(response.status_code, 200)

        incoming_response = response.json()

        self.assertEqual(expected_response, incoming_response)

    def test_validate_date_valid(self):
        self.assertTrue(validate_date('2024-02-28'))

    def test_validate_date_invalid(self):
        self.assertFalse(validate_date('invalid_date'))

    def test_validate_currencies_valid(self):
        self.assertTrue(validate_currencies(['EUR', 'USD']))

    def test_validate_currencies_invalid(self):
        self.assertFalse(validate_currencies(['invalid', 'currency']))

    def test_validate_amount_valid(self):
        self.assertTrue(validate_amount('50.46'))

    def test_validate_amount_invalid(self):
        self.assertFalse(validate_amount('invalid_amount'))

    def test_validate_base_currency_valid(self):
        self.assertTrue(validate_base_currency('USD'))

    def test_validate_base_currency_invalid(self):
        self.assertFalse(validate_base_currency('invalid_currency'))


if __name__ == '__main__':
    unittest.main()
