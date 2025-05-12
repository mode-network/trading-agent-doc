# Mode Trade - trading bot

**https://trade.mode.network**

1. Go to https://github-dev.orderly.network/broker-registration
2. Connect your wallet
3. Select "EOA wallet"
4. Select the broker id Mode or enter manually "mode"
5. Click on "Register Account" and sign the message
6. Select scope "read,trading" and click on "Create Orderly key" and sign the message (the key will expire in 1 year)
7. Copy your Orderly account ID, Orderly public key and private key
8. Create the `.env` file based on the example and populate the values
9. You can deposit: go to the "Assets" tab, enter an amount and proceed to the deposit

You can also deposit and withdraw from the Mode Trade UI: https://trade.mode.network

## CCXT

### Installation

    python3.10 -m venv venv
    source venv/bin/activate
    pip install -r requirements

### Usage

You can use the beta version of the `ccxt` library for Mode Trade exchange.

```python
import mode_trade

exchange = mode_trade.modetrade(
    {
        "apiKey": os.environ.get("MODE_TRADE_PUBLIC_KEY"),
        "secret": os.environ.get("MODE_TRADE_PRIVATE_KEY"),
        "accountId": os.environ.get("MODE_TRADE_ACCOUNT_ID")
    }
)
```

### Run the example

    python example_ccxt.py

## Freqtrade

Once you have your Orderly account ID, public key, and private key, you can use them to configure the Freqtrade bot. The following steps will guide you through the process of setting up Freqtrade with the Mode Trade exchange.

- `freqtrade create-userdir --userdir data`
- `freqtrade trade --userdir data --strategy SampleStrategy`

`config.json`

```json
{
  "exchange": {
    "name": "modetrade",
    "key": "orderly public key",
    "secret": "orderly secret key",
    "accountId": "orderly account id"
  }
}
```

# Disclaimer

This project is for educational purposes only. It is not intended to be used for trading or investment purposes. The authors and contributors are not responsible for any losses or damages that may occur as a result of using this project. Always do your own research and consult with a financial advisor before making any investment decisions.

# License

This project is licensed under the MIT License.
