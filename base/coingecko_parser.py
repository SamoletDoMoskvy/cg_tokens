import shutil
import requests

from cg_tokens.settings import STATIC_ROOT
from tokens_app.models import Token

COINGECKO_URL = 'https://api.coingecko.com/api/v3/coins/'


def get_coingecko_tokens(url: str) -> list:
    """
    Возвращает список всех токенов CoinGecko
    """
    url += 'list'
    params = {
        'include_platform': 'true',
    }
    return requests.get(
        url=url,
        params=params,
    ).json()


def get_popular_coingecko_tokens(url: str) -> list:
    """
    Возвращает список из 50 самых популярных токенов с CoinGecko
    """
    return requests.get(url).json()


def get_token_image(url: str, address: str):
    """
    Записывает логотип токена на диск
    """
    r = requests.get(url,
                     headers={
                         'User-Agent': 'My User Agent 1.0',
                         # 'From': 'youremail@domain.com'  # This is another valid field
                     },
                     stream=True)
    filepath = STATIC_ROOT / "tokens" / f"{address}.png"
    if r.status_code == 200:
        with open(filepath, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)


def parse_coingecko_tokens():
    """
    Парсит данные из источника и записывает их в БД,
    также подтягивает пикчу токена в диру со статикой
    """
    popular_tokens = get_popular_coingecko_tokens(COINGECKO_URL)
    tokens = get_coingecko_tokens(COINGECKO_URL)

    for popular_token in popular_tokens:
        for token in tokens:
            if popular_token['id'] == token['id'] \
                    and popular_token['symbol'] == token['symbol'] \
                    and popular_token['name'] == token['name']:

                if 'ethereum' in token['platforms'].keys():
                    address = token['platforms']['ethereum']
                else:
                    address = 'Undefined address'

                name = token['name']
                symbol = token['symbol']
                price_in_dollars = popular_token['market_data']['current_price']['usd']

                try:
                    token_object = Token.objects.get(
                        address=address,
                        name=name,
                        symbol=symbol,
                    )
                    token_object.price_in_dollars = price_in_dollars
                    token_object.save()

                except Token.DoesNotExist:
                    token_object = Token.objects.create(
                        address=address,
                        name=name,
                        symbol=symbol,
                        price_in_dollars=price_in_dollars,
                    )
                    token_object.save()
                get_token_image(
                    address=address,
                    url=popular_token['image']['large']
                )
