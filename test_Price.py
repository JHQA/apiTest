import unittest
import requests

# Credentials
email = ''
apiKey = ''

# API point and options
url = 'https://api.cryptowat.ch/markets'
bitfinex_btcusd = '/bitfinex/btcusd'
bitfinex_ltcusd = '/bitfinex/ltcusd'
bitfinex_ltcbtc = '/bitfinex/ltcbtc'
bitfinex_ethusd = '/bitfinex/ethusd'
bitfinex_ethbtc = '/bitfinex/ethbtc'
options = {'timeout':4}

class TestPrices(unittest.TestCase):

    # Verify the market/prices endpoint
    def test_market_prices(self):
        resp = requests.get(url + '/prices', auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertGreater(jsonData["index:kraken-futures:cf-in-bchusd"], 0, 'market/prices "index:kraken-futures:cf-in-bchusd" was not greater than zero')
        self.assertGreater(jsonData["market:binance-us:1inchusd"], 0, 'market/prices "market:binance-us:1inchusd" was not greater than zero')
        self.assertGreater(jsonData["market:bitfinex:iceusd"], 0, 'market/prices "market:bitfinex:iceusd" was not greater than zero')
        self.assertGreater(jsonData["market:gateio:lgcyusdt"], 0, 'market/prices "market:gateio:lgcyusdt" was not greater than zero')
        self.assertGreater(jsonData["market:luno:btczar"], 0, 'market/prices "market:luno:btczar" was not greater than zero')

        self.assertGreater(allowData['cost'], 0, '/market/prices allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, '/market/prices allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", '/market/prices upgrade message was incorrect')

    # Verify the bitfinex btcusd price endpoint
    def test_bitfinex_btcusd(self):
        resp = requests.get(url + bitfinex_btcusd + '/price', auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')
        self.assertGreater(jsonData['price'], 0, 'btcusd/price was not a positive number')

        self.assertGreater(allowData['cost'], 0, 'bitfinex btcusd allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, 'bitfinex btcusd allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", 'bitfinex btcusd upgrade message was incorrect')

    # Verify the bitfinex ltcusd price endpoint
    def test_bitfinex_ltcusd(self):
        resp = requests.get(url + bitfinex_ltcusd + '/price', auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')
        self.assertGreater(jsonData['price'], 0, 'ltcusd/price was not a positive number')

        self.assertGreater(allowData['cost'], 0, 'bitfinex ltcusd allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, 'bitfinex ltcusd allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", 'bitfinex ltcusd upgrade message was incorrect')

    # Verify the bitfinex ltcbtc price endpoint
    def test_bitfinex_ltcbtc(self):
        resp = requests.get(url + bitfinex_ltcbtc + '/price', auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')
        self.assertGreater(jsonData['price'], 0, 'ltcbtc/price was not a positive number')

        self.assertGreater(allowData['cost'], 0, 'bitfinex ltcbtc cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, 'bitfinex ltcbtc remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", 'bitfinex ltcbtc upgrade message was incorrect')

    # Verify the bitfinex ethusd price endpoint
    def test_bitfinex_ethusd(self):
        resp = requests.get(url + bitfinex_ethusd + '/price', auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')
        self.assertGreater(jsonData['price'], 0, 'ethusd/price was not a positive number')
        
        self.assertGreater(allowData['cost'], 0, 'bitfinex ethusd cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, 'bitfinex ethusd remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", 'bitfinex ethusd upgrade message was incorrect')


    # Verify the bitfinex ethbtc price endpoint
    def test_bitfinex_ethbtc(self):
        resp = requests.get(url + bitfinex_ethbtc +'/price', auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')
        self.assertGreater(jsonData['price'], 0, 'ethbtc/price was not a positive number')

        self.assertGreater(allowData['cost'], 0, 'bitfinex ethbtc cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, 'bitfinex ethbtc remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", 'bitfinex ethbtc upgrade message was incorrect')

