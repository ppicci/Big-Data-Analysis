import requests
import time


def file_parser(filepath):
    data_list = []
    with open(filepath) as file:
        for line in file:
            line = line.strip().split(',')
            data_list.append((int(line[0]), line[1], line[2]))

    return data_list


def conversion_getter(data):
    amount, from_currency, to_currency = data

    url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        rate = data['rates'][to_currency]

        return (f"{amount} {from_currency} = {rate} {to_currency}")
    else:
        return ("Try again later")
