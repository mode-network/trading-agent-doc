import os


from dotenv import load_dotenv


import mode_trade
from utils import account_id_from_address


load_dotenv()


# Mode trade exchange:
exchange = mode_trade.modetrade(
    {
        "apiKey": os.environ.get("MODE_TRADE_PUBLIC_KEY"),
        "secret": os.environ.get("MODE_TRADE_PRIVATE_KEY"),
        "accountId": os.environ.get("MODE_TRADE_ACCOUNT_ID")
        or account_id_from_address(os.environ.get("MODE_TRADE_ADDRESS", "")),
    }
)

# Load the markets to get trading pairs info.
markets = exchange.load_markets()
print("markets:", markets)
currencies = exchange.fetch_currencies()
print("currencies:", currencies)
balance = exchange.fetch_balance()
print("balance: ", balance)
