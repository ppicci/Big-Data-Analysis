import threading
import requests
import time


conversion_requests = [
    (100, "USD", "EUR"),
    (200, "EUR", "GBP"),
    (300, "GBP", "USD"),
    (150, "USD", "JPY"),
    (250, "JPY", "INR"),
    (350, "INR", "CNY"),
    (400, "CNY", "AUD"),
    (500, "AUD", "CAD"),
    (600, "CAD", "CHF"),
    (700, "CHF", "USD")
]
connection_semaphore = threading.Semaphore(3)
def conversion_getter(data):
    amount, from_currency, to_currency = data

    connection_semaphore.acquire()

    url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()

            rate = data['rates'][to_currency]
            return (f"{amount} {from_currency} = {rate} {to_currency}")
        else:
            return ("Try again later")
    finally:
        connection_semaphore.release()

def thread_printer(data):
    print(conversion_getter(data))