import requests
import json
from config import keys

class ConvertException(Exception):
    pass

class СurrencyConverter:
    @staticmethod
    def currency_convert(qoute: str, base: str, amount: str):

        if qoute == base:
            raise ConvertException('Должны быть разные валюты')

        try:
            qoute_name = keys[qoute]
        except KeyError:
            raise ConvertException(f'Не удалось обработать валюту {qoute}')

        try:
            base_name = keys[base]
        except KeyError:
            raise ConvertException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except KeyError:
            raise ConvertException(f'Не удалось обработать количество {amount}')

        res = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={qoute_name}&tsyms={base_name}')

        float_value = json.loads(res.content)[keys[base]]
        total_base = round(amount * float_value,3)

        return total_base