import currencyapicom
from everapi import ApiError


def get_client_api():
    """
    Function to create and return an instance of the currencyapicom.Client.

    Returns:
        currencyapicom.Client: Instance of the currencyapicom.Client or None if an error occurs.
    """

    try:
        client = currencyapicom.Client(
            'cur_live_ua5A26uZHtydGAvuoRnDLazKMfUFZVvhQWRS5CBu'
        )
        return client
    except Exception as e:
        print(f"Error while creating API client: {e}")
        return None


def api_currency_data(date: str, base_currency: str, currencies: list):
    """
    Function to fetch currency exchange rate data from an external API.

    Args:
        date (str): Date for which currency exchange rates are requested.
        base_currency (str): The base currency for conversion.
        currencies (list): List of target currencies to retrieve exchange rates for.

    Returns:
        dict or bool: Dictionary containing currency exchange rate data for the specified date,
                      or False if an error occurs.
    """
    client = get_client_api()
    response = None

    try:
        response = client.historical(date, base_currency, currencies)
    except ApiError:
        print('Please check your input data or API-KEY')

    if response:
        data = response.get('data', None)

        if data is None:
            print(response.get('message'))  # Czasami API nie ma danych np. 2022-02-02
            return False
        else:
            return data
