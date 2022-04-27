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
options = {'limit': 5, 'timeout':4}

# Verify https://api.cryptowat.ch/markets/:exchange/:pair
class TestDetails(unittest.TestCase):

    # Verify the markets/bitfinex/btcusd endpoint
    def test_bitfinex_btcusd_details(self):
        resp = requests.get(url + bitfinex_btcusd, auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')
        self.assertEqual(jsonData['id'], 1, 'market btcusd has an incorrect ID')
        self.assertEqual(jsonData['exchange'], 'bitfinex', 'market /bitfinex/btcusd has an incorrect exchange')
        self.assertEqual(jsonData['pair'], 'btcusd', 'market /bitfinex/btcusd has an incorrect pair')
        self.assertEqual(jsonData['active'], True, 'market /bitfinex/btcusd is not active')

        self.assertGreater(allowData['cost'], 0, '/bitfinex/btcusd allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, '/bitfinex/btcusd allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", '/bitfinex/btcusd upgrade message was incorrect')

        self.assertEqual(jsonData['routes']['price'], "https://api.cryptowat.ch/markets/bitfinex/btcusd/price", 'bitfinex btcusd has an incorrect price route')
        self.assertEqual(jsonData['routes']['summary'], "https://api.cryptowat.ch/markets/bitfinex/btcusd/summary", 'bitfinex btcusd has an incorrect summary route')
        self.assertEqual(jsonData['routes']['orderbook'], "https://api.cryptowat.ch/markets/bitfinex/btcusd/orderbook", 'bitfinex btcusd has an incorrect orderbook route')
        self.assertEqual(jsonData['routes']['trades'], "https://api.cryptowat.ch/markets/bitfinex/btcusd/trades", 'bitfinex btcusd has an incorrect trades route')
        self.assertEqual(jsonData['routes']['ohlc'], "https://api.cryptowat.ch/markets/bitfinex/btcusd/ohlc", 'bitfinex btcusd has an incorrect ohlc route')

    # Verify the markets/bitfinex/ltcusd endpoint
    def test_bitfinex_ltcusd_details(self):
        resp = requests.get(url + bitfinex_ltcusd, auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')
        self.assertEqual(jsonData['id'], 2, 'market ltcusd has an incorrect ID')
        self.assertEqual(jsonData['exchange'], 'bitfinex', 'market /bitfinex/ltcusd has an incorrect exchange')
        self.assertEqual(jsonData['pair'], 'ltcusd', 'market /bitfinex/ltcusd has an incorrect pair')
        self.assertEqual(jsonData['active'], True, 'market /bitfinex/ltcusd is not active')

        self.assertGreater(allowData['cost'], 0, 'bitfinex ltcusd allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, 'bitfinex ltcusd allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", 'bitfinex ltcusd upgrade message was incorrect')

        self.assertEqual(jsonData['routes']['price'], "https://api.cryptowat.ch/markets/bitfinex/ltcusd/price", 'bitfinex ltcusd has an incorrect price route')
        self.assertEqual(jsonData['routes']['summary'], "https://api.cryptowat.ch/markets/bitfinex/ltcusd/summary", 'bitfinex ltcusd has an incorrect summary route')
        self.assertEqual(jsonData['routes']['orderbook'], "https://api.cryptowat.ch/markets/bitfinex/ltcusd/orderbook", 'bitfinex ltcusd has an incorrect orderbook route')
        self.assertEqual(jsonData['routes']['trades'], "https://api.cryptowat.ch/markets/bitfinex/ltcusd/trades", 'bitfinex ltcusd has an incorrect trades route')
        self.assertEqual(jsonData['routes']['ohlc'], "https://api.cryptowat.ch/markets/bitfinex/ltcusd/ohlc", 'bitfinex ltcusd has an incorrect ohlc route')

    # Verify the markets/bitfinex/ltcbtc endpoint
    def test_bitfinex_ltcbtc_details(self):
        resp = requests.get(url + bitfinex_ltcbtc, auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')
        self.assertEqual(jsonData['id'], 3, 'market ltcbtc has an incorrect ID')
        self.assertEqual(jsonData['exchange'], 'bitfinex', 'market ltcbtc has an incorrect exchange')
        self.assertEqual(jsonData['pair'], 'ltcbtc', 'market ltcbtc has an incorrect pair')
        self.assertEqual(jsonData['active'], True, 'market ltcbtc is not active')

        self.assertGreater(allowData['cost'], 0, 'bitfinex ltcbtc allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, 'bitfinex ltcbtc allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", 'bitfinex ltcbtc upgrade message was incorrect')

        self.assertEqual(jsonData['routes']['price'], "https://api.cryptowat.ch/markets/bitfinex/ltcbtc/price", 'bitfinex ltcbtc has an incorrect price route')
        self.assertEqual(jsonData['routes']['summary'], "https://api.cryptowat.ch/markets/bitfinex/ltcbtc/summary", 'bitfinex ltcbtc has an incorrect summary route')
        self.assertEqual(jsonData['routes']['orderbook'], "https://api.cryptowat.ch/markets/bitfinex/ltcbtc/orderbook", 'bitfinex ltcbtc has an incorrect orderbook route')
        self.assertEqual(jsonData['routes']['trades'], "https://api.cryptowat.ch/markets/bitfinex/ltcbtc/trades", 'bitfinex ltcbtc has an incorrect trades route')
        self.assertEqual(jsonData['routes']['ohlc'], "https://api.cryptowat.ch/markets/bitfinex/ltcbtc/ohlc", 'bitfinex ltcbtc has an incorrect ohlc route')

    # Verify the markets/bitfinex/ethusd endpoint
    def test_bitfinex_ethusd_details(self):
        resp = requests.get(url + bitfinex_ethusd, auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')
        self.assertEqual(jsonData['id'], 4, 'market ethusd has an incorrect ID')
        self.assertEqual(jsonData['exchange'], 'bitfinex', 'market ethusd has an incorrect exchange')
        self.assertEqual(jsonData['pair'], 'ethusd', 'market ethusd has an incorrect pair')
        self.assertEqual(jsonData['active'], True, 'market ethusd is not active')

        self.assertGreater(allowData['cost'], 0, 'bitfinex ethusd allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, 'bitfinex ethusd allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", 'bitfinex ethusd upgrade message was incorrect')

        self.assertEqual(jsonData['routes']['price'], "https://api.cryptowat.ch/markets/bitfinex/ethusd/price", 'bitfinex ethusd has an incorrect price route')
        self.assertEqual(jsonData['routes']['summary'], "https://api.cryptowat.ch/markets/bitfinex/ethusd/summary", 'bitfinex ethusd has an incorrect summary route')
        self.assertEqual(jsonData['routes']['orderbook'], "https://api.cryptowat.ch/markets/bitfinex/ethusd/orderbook", 'bitfinex ethusd has an incorrect orderbook route')
        self.assertEqual(jsonData['routes']['trades'], "https://api.cryptowat.ch/markets/bitfinex/ethusd/trades", 'bitfinex ethusd has an incorrect trades route')
        self.assertEqual(jsonData['routes']['ohlc'], "https://api.cryptowat.ch/markets/bitfinex/ethusd/ohlc", 'bitfinex ethusd has an incorrect ohlc route')

    # Verify the markets/bitfinex/ethbtc endpoint
    def test_bitfinex_ethbtc_details(self):
        resp = requests.get(url + bitfinex_ethbtc, auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')
        self.assertEqual(jsonData['id'], 5, 'market ethbtc has an incorrect ID')
        self.assertEqual(jsonData['exchange'], 'bitfinex', 'market ethbtc has an incorrect exchange')
        self.assertEqual(jsonData['pair'], 'ethbtc', 'market ethbtc has an incorrect pair')
        self.assertEqual(jsonData['active'], True, 'market ethbtc is not active')

        self.assertGreater(allowData['cost'], 0, 'bitfinex ethbtc allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, 'bitfinex ethbtc allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", 'bitfinex ethbtc upgrade message was incorrect')

        self.assertEqual(jsonData['routes']['price'], "https://api.cryptowat.ch/markets/bitfinex/ethbtc/price", 'bitfinex ethbtc has an incorrect price route')
        self.assertEqual(jsonData['routes']['summary'], "https://api.cryptowat.ch/markets/bitfinex/ethbtc/summary", 'bitfinex ethbtc has an incorrect summary route')
        self.assertEqual(jsonData['routes']['orderbook'], "https://api.cryptowat.ch/markets/bitfinex/ethbtc/orderbook", 'bitfinex ethbtc has an incorrect orderbook route')
        self.assertEqual(jsonData['routes']['trades'], "https://api.cryptowat.ch/markets/bitfinex/ethbtc/trades", 'bitfinex ethbtc has an incorrect trades route')
        self.assertEqual(jsonData['routes']['ohlc'], "https://api.cryptowat.ch/markets/bitfinex/ethbtc/ohlc", 'bitfinex ethbtc has an incorrect ohlc route')
