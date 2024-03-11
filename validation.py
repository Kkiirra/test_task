from datetime import datetime
from api_key import get_client_api
import requests

def valid_list_currencies():
    """
    Function to retrieve and validate the list of available currencies from the API.

    Returns:
        dict or False: Dictionary containing allowed currencies or False if an error occurs.
    """
    try:
        client = get_client_api()
        if client:
            result = client.currencies()
            allowed_currencies = result.get('data').keys()
            return allowed_currencies
        else:
            print("Currency list data failed.")
            return False
    except Exception as e:
        print(f"Error while validating currencies: {e}")
        return False


def validate_date(date_str: str, format_str="%Y-%m-%d") -> bool:
    """
    Function to validate a date string.

    Args:
        date_str (str): Date string to validate.
        format_str (str): Format string for the expected date format (default is "%Y-%m-%d").

    Returns:
        bool: True if the date string is valid, False otherwise.
    """
    try:
        datetime.strptime(date_str, format_str)
        return True
    except ValueError:
        return False


def validate_currencies(input_currencies: list) -> bool:
    """
    Function to validate a list of currencies.

    Args:
        input_currencies (list): List of currency codes to validate.

    Returns:
        bool: True if all currencies in the list are valid, False otherwise.
    """
    list_of_currencies = valid_list_currencies()
    if list_of_currencies:
        return all(currency.upper() in list_of_currencies for currency in input_currencies)
    else:
        return False


def validate_amount(amount_str: str) -> bool:
    """
    Function to validate an amount string.

    Args:
        amount_str (str): Amount string to validate.

    Returns:
        bool: True if the amount string is valid, False otherwise.
    """
    return amount_str.replace('.', '', 1).isdigit()


def validate_base_currency(input_base_currency: str) -> bool:
    """
    Function to validate a base currency.

    Args:
        input_base_currency (str): Base currency code to validate.

    Returns:
        bool: True if the base currency is valid, False otherwise.
    """
    list_of_currencies = valid_list_currencies()
    if list_of_currencies:
        return input_base_currency.upper() in list_of_currencies
    else:
        return False


if __name__ == '__main__':
    a = requests.post('http://127.0.0.1:8000/exchange/', json={
            "input_currency": "USD",
            "output_currencies": ['EUR', 'GBP'],
            "amount": 50.46,
            "date": "2021-02-23"
        })
    print(a.json())
