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

class TestOHLC(unittest.TestCase):

    # Verify the /bitfinex/btcusd/ohlc endpoint
    def test_bitfinex_btcusd_ohlc(self):
        resp = requests.get(url + bitfinex_btcusd +'/ohlc', auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertEqual(jsonData['14400'][0][0] % 60, 0, '/bitfinex/btcusd/ohlc the first iterable was not in a 60 minute format')
        self.assertTrue((len(jsonData['14400'][0]) == 7), '/bitfinex/btcusd/ohlc list was not the correct length')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData['14400'][0]), '/bitfinex/btcusd/ohlc did not return a list of numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData['14400'][1]), '/bitfinex/btcusd/ohlc did not return a list of numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData['14400'][2]), '/bitfinex/btcusd/ohlc did not return a list of numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData['14400'][3]), '/bitfinex/btcusd/ohlc did not return a list of numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData['14400'][4]), '/bitfinex/btcusd/ohlc did not return a list of numbers')

        self.assertGreater(allowData['cost'], 0, '/bitfinex/btcusd/ohlc allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, '/bitfinex/btcusd/ohlc allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", '/bitfinex/btcusd/ohlc upgrade message was incorrect')

    # Verify the /bitfinex/ltcusd/ohlc endpoint
    def test_bitfinex_ltcusd_ohlc(self):
        resp = requests.get(url + bitfinex_ltcusd +'/ohlc', auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertEqual(jsonData['14400'][0][0] % 60, 0, '/bitfinex/ltcusd/ohlc the first iterable was not in a 60 minute format')
        self.assertTrue((len(jsonData['14400'][0]) == 7), '/bitfinex/ltcusd/ohlc list was not the correct length')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData['14400'][0]), '/bitfinex/ltcusd/ohlc did not return a list of numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData['14400'][1]), '/bitfinex/ltcusd/ohlc did not return a list of numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData['14400'][2]), '/bitfinex/ltcusd/ohlc did not return a list of numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData['14400'][3]), '/bitfinex/ltcusd/ohlc did not return a list of numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData['14400'][4]), '/bitfinex/ltcusd/ohlc did not return a list of numbers')

        self.assertGreater(allowData['cost'], 0, '/bitfinex/ltcusd/ohlc allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, '/bitfinex/ltcusd/ohlc allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", '/bitfinex/ltcusd/ohlc upgrade message was incorrect')

    # Verify the /bitfinex/ltcbtc/ohlc endpoint
    def test_bitfinex_ltcbtc_ohlc(self):
        resp = requests.get(url + bitfinex_ltcbtc +'/ohlc', auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertEqual(jsonData['14400'][0][0] % 60, 0, '/bitfinex/ltcbtc/ohlc the first iterable was not in a 60 minute format')
        self.assertTrue((len(jsonData['14400'][0]) == 7), '/bitfinex/ltcbtc/ohlc list was not the correct length')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData['14400'][0]), '/bitfinex/ltcbtc/ohlc did not return a list of numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData['14400'][1]), '/bitfinex/ltcbtc/ohlc did not return a list of numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData['14400'][2]), '/bitfinex/ltcbtc/ohlc did not return a list of numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData['14400'][3]), '/bitfinex/ltcbtc/ohlc did not return a list of numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData['14400'][4]), '/bitfinex/ltcbtc/ohlc did not return a list of numbers')

        self.assertGreater(allowData['cost'], 0, '/bitfinex/ltcbtc/ohlc allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, '/bitfinex/ltcbtc/ohlc allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", '/bitfinex/ltcbtc/ohlc upgrade message was incorrect')

    # Verify the /bitfinex/ethusd/ohlc endpoint
    def test_bitfinex_ethusd_ohlc(self):
        resp = requests.get(url + bitfinex_ethusd +'/ohlc', auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertEqual(jsonData['14400'][0][0] % 60, 0, '/bitfinex/ethusd/ohlc the first iterable was not in a 60 minute format')
        self.assertTrue((len(jsonData['14400'][0]) == 7), '/bitfinex/ethusd/ohlc list was not the correct length')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData['14400'][0]), '/bitfinex/ethusd/ohlc did not return a list of numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData['14400'][1]), '/bitfinex/ethusd/ohlc did not return a list of numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData['14400'][2]), '/bitfinex/ethusd/ohlc did not return a list of numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData['14400'][3]), '/bitfinex/ethusd/ohlc did not return a list of numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData['14400'][4]), '/bitfinex/ethusd/ohlc did not return a list of numbers')

        self.assertGreater(allowData['cost'], 0, '/bitfinex/ethusd/ohlc allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, '/bitfinex/ethusd/ohlc allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", '/bitfinex/ethusd/ohlc upgrade message was incorrect')

    # Verify the /bitfinex/ethbtc/ohlc endpoint
    def test_bitfinex_ethbtc_ohlc(self):
        resp = requests.get(url + bitfinex_ethbtc +'/ohlc', auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertEqual(jsonData['14400'][0][0] % 60, 0, '/bitfinex/ethbtc/ohlc the first iterable was not in a 60 minute format')
        self.assertTrue((len(jsonData['14400'][0]) == 7), '/bitfinex/ethbtc/ohlc list was not the correct length')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData['14400'][0]), '/bitfinex/ethbtc/ohlc did not return a list of numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData['14400'][1]), '/bitfinex/ethbtc/ohlc did not return a list of numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData['14400'][2]), '/bitfinex/ethbtc/ohlc did not return a list of numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData['14400'][3]), '/bitfinex/ethbtc/ohlc did not return a list of numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData['14400'][4]), '/bitfinex/ethbtc/ohlc did not return a list of numbers')

        self.assertGreater(allowData['cost'], 0, '/bitfinex/ethbtc/ohlc allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, '/bitfinex/ethbtc/ohlc allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", '/bitfinex/ethbtc/ohlc upgrade message was incorrect')
