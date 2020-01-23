import requests


#https://yobit.net/api/2/


def get_btc(val):
    url = f'https://yobit.net/api/2/{val}_usd/ticker'
    r = requests.get(url).json()
    price = r['ticker']['last']
    return str(price) + ' USD'







