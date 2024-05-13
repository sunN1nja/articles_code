import requests

def get_exchange_rate(api_key, base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        exchange_rate = data['conversion_rates'][target_currency]
        return exchange_rate
    else:
        print("Ошибка при получении данных с сервера.")
        return None

def convert_currency(api_key, amount, base_currency, target_currency):
    rate = get_exchange_rate(api_key, base_currency, target_currency)
    if rate is not None:
        converted_amount = rate * amount
        print(f"{amount} {base_currency} равно {converted_amount:.2f} {target_currency}")
    else:
        print("Не удалось конвертировать валюту.")

if __name__ == "__main__":
    api_key = "ВАШ_КЛЮЧ_API"
    base_currency = "USD"
    target_currency = "RUB"
    amount = 100

    convert_currency(api_key, amount, base_currency, target_currency)