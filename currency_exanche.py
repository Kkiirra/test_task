from get_input import get_inputs
from api_key import api_currency_data


def exchange_currency(date: str, base_currency: str, currencies: list, amount: float, response=None):
    data = api_currency_data(date, base_currency, currencies)
    """
    Function to exchange currency.

    Args:
        date (str): Date for which currency exchange rates are requested.
        base_currency (str): The base currency for conversion.
        currencies (list): List of target currencies to convert to.
        amount (float): Amount of base currency to convert.
        response (Optional): Additional response data (default is None).

    Returns:
        None: The function prints the exchanged currency values.
    """
    print('Data for', date)
    for currency, info in data.items():
        currency_exchange = info.get('value', None)
        if currency_exchange:
            exchanged_value = currency_exchange * amount
            print(f" -> {amount:.2f} {base_currency} = {exchanged_value:.2f} {currency}")


if __name__ == "__main__":
    try:
        inputs = get_inputs()
        if inputs:
            date, base_currency, amount, currencies = inputs
            exchange_currency(date, base_currency, currencies, amount)
    except KeyboardInterrupt:
        print("\nExiting program...")
    except Exception as e:
        print('Unexpected ERROR', e)
