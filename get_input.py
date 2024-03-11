import math
from validation import *


def get_inputs():
    """
    Function to get user inputs for base currency, target currencies, amount, and date.

    Returns:
        tuple: Tuple containing user inputs (date, base_currency, amount, currencies).
    """
    base_currency_input = get_base_currency_input()
    currencies_input = get_currencies_input()
    amount_input = get_amount_input()
    date_input = get_date_input()
    return date_input, base_currency_input, amount_input, currencies_input


def get_date_input():
    """
    Function to get user input for the date.

    Returns:
        str: Validated date input in the format YYYY-MM-DD.
    """
    while True:
        date_input = input("Enter date YYYY-MM-DD: ")
        if not date_input or not validate_date(date_input):
            print("Error: Please, try again.")
            continue
        return date_input


def get_currencies_input():
    """
    Function to get user input for the target currencies.

    Returns:
        list: List of validated target currencies.
    """
    while True:
        currency_input = [currency.strip().upper() for currency in input("Enter output currencies: ").split(',')]
        if not currency_input or not validate_currencies(currency_input):
            print("Error: Please, try again.")
            continue
        return currency_input


def get_base_currency_input():
    """
    Function to get user input for the base currency.

    Returns:
        str: Validated base currency input.
    """
    while True:
        currency_input = input("Enter input Currency: ")
        if not currency_input or not validate_base_currency(currency_input):
            print("Error: Please, try again.")
            continue
        return currency_input.upper()


def get_amount_input():
    """
    Function to get user input for the amount.

    Returns:
        float: Validated and rounded amount input.
    """
    while True:
        amount_input = input("Enter Amount: ")
        if not amount_input or not validate_amount(amount_input):
            print("Error: Please, try again.")
            continue
        return math.ceil(float(amount_input) * 100) / 100  # return round(float(value_input), 2)
