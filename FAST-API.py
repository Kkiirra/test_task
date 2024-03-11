import uvicorn
from fastapi import FastAPI
from typing import List, Dict, Union
from api_key import api_currency_data

app = FastAPI()


@app.post("/exchange/")
async def exchange_currency(data: Dict[str, Union[str, List[str], float]]) -> List[Dict[str, str]]:
    """
    Handler for POST requests to /exchange/. Accepts data about date, base currency,currency,
    amount for conversion.

    Args:
        data (dict): Dictionary containing information about currency and amount.

    Returns:
        list: List of dictionaries with data about the converted amount for each currency.
    """

    input_currency, output_currencies, amount, date = (
        data["input_currency"], data["output_currencies"], data["amount"], data["date"]
    )

    currency_api_data = api_currency_data(date, input_currency, output_currencies)

    array = []
    for currency, info in currency_api_data.items():
        currency_exchange = info.get('value', 0)
        array.append({
            "currency": currency,
            "amount": f'{float(amount) * float(currency_exchange)}',
        })
    return array


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
