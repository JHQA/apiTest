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

# Verify https://api.cryptowat.ch/markets/:exchange/:pair/trades
class TestTrades(unittest.TestCase):

    # Verify the bitfinex/btcusd/trades endpoint
    def test_bitfinex_btcusd_trades(self):
        resp = requests.get(url + bitfinex_btcusd + '/trades', auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, 'The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertEqual(len(jsonData), 5, 'bitfinex/btcusd trades is missing list data')
        self.assertEqual(jsonData[0][0], 0, 'bitfinex/btcusd trades ID was not correct')
        self.assertGreater(jsonData[0][1], 0, 'bitfinex/btcusd trades timestamp was not greater than zero')
        self.assertGreater(jsonData[0][2], 0, 'bitfinex/btcusd trades price was not greater than zero')
        self.assertGreater(jsonData[0][3], 0, 'bitfinex/btcusd trades amount was not greater than zero')

        self.assertGreater(allowData['cost'], 0, 'bitfinex/btcusd/trades allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, 'bitfinex/btcusd/trades allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", 'bitfinex/btcusd/trades upgrade message was incorrect')

    # Verify the bitfinex/ltcusd/trades endpoint
    def test_bitfinex_ltcusd_trades(self):
        resp = requests.get(url + bitfinex_ltcusd + '/trades', auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, 'The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertEqual(len(jsonData), 5, 'bitfinex/ltcusd trades is missing list data')
        self.assertEqual(jsonData[0][0], 0, 'bitfinex/ltcusd trades ID was not correct')
        self.assertGreater(jsonData[0][1], 0, 'bitfinex/ltcusd trades timestamp was not greater than zero')
        self.assertGreater(jsonData[0][2], 0, 'bitfinex/ltcusd trades price was not greater than zero')
        self.assertGreater(jsonData[0][3], 0, 'bitfinex/ltcusd trades amount was not greater than zero')

        self.assertGreater(allowData['cost'], 0, '/market/bitfinex/ltcusd/trades allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, '/market/bitfinex/ltcusd/trades allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", '/market/bitfinex/ltcusd/trades upgrade message was incorrect')

    # Verify the bitfinex/ltcbtc/trades endpoint
    def test_bitfinex_ltcbtc_trades(self):
        resp = requests.get(url + bitfinex_ltcbtc + '/trades', auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, 'The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertEqual(len(jsonData), 5, 'bitfinex/ltcbtc trades is missing list data')
        self.assertEqual(jsonData[0][0], 0, 'bitfinex/ltcbtc trades ID was not correct')
        self.assertGreater(jsonData[0][1], 0, 'bitfinex/ltcbtc trades timestamp was not greater than zero')
        self.assertGreater(jsonData[0][2], 0, 'bitfinex/ltcbtc trades price was not greater than zero')
        self.assertGreater(jsonData[0][3], 0, 'bitfinex/ltcbtc trades amount was not greater than zero')

        self.assertGreater(allowData['cost'], 0, '/market/bitfinex/ltcbtc/trades allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, '/market/bitfinex/ltcbtc/trades allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", '/market/bitfinex/ltcbtc/trades upgrade message was incorrect')

    # Verify the bitfinex/ethusd/trades endpoint
    def test_bitfinex_ethusd_trades(self):
        resp = requests.get(url + bitfinex_ethusd + '/trades', auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, 'The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertEqual(len(jsonData), 5, 'bitfinex/ethusd trades is missing list data')
        self.assertEqual(jsonData[0][0], 0, 'bitfinex/ethusd trades ID was not correct')
        self.assertGreater(jsonData[0][1], 0, 'bitfinex/ethusd trades timestamp was not greater than zero')
        self.assertGreater(jsonData[0][2], 0, 'bitfinex/ethusd trades price was not greater than zero')
        self.assertGreater(jsonData[0][3], 0, 'bitfinex/ethusd trades amount was not greater than zero')

        self.assertGreater(allowData['cost'], 0, '/market/bitfinex/ethusd/trades allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, '/market/bitfinex/ethusd/trades allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", '/market/bitfinex/ethusd/trades upgrade message was incorrect')

    # Verify the bitfinex/ethbtc/trades endpoint
    def test_bitfinex_ethbtc_trades(self):
        resp = requests.get(url + bitfinex_ethbtc + '/trades', auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, 'The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertEqual(len(jsonData), 5, 'bitfinex/ethbtc trades is missing list data')
        self.assertEqual(jsonData[0][0], 0, 'bitfinex/ethbtc trades ID was not correct')
        self.assertGreater(jsonData[0][1], 0, 'bitfinex/ethbtc trades timestamp was not greater than zero')
        self.assertGreater(jsonData[0][2], 0, 'bitfinex/ethbtc trades price was not greater than zero')
        self.assertGreater(jsonData[0][3], 0, 'bitfinex/ethbtc trades amount was not greater than zero')

        self.assertGreater(allowData['cost'], 0, '/market/bitfinex/ethbtc/trades allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, '/market/bitfinex/ethbtc/trades allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", '/market/bitfinex/ethbtc/trades upgrade message was incorrect')
