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

# Verify https://api.cryptowat.ch/markets/:exchange/:pair/summary
class TestOneSum(unittest.TestCase):
    # Verify the bitfinex/btcusd/summary endpoint
    def test_bitfinex_btcusd_summary(self):
        resp = requests.get(url + bitfinex_btcusd + '/summary', auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        priceData = resp.json()['result']['price']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, 'The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertGreaterEqual(priceData['high'], priceData['low'], 'bitfinex/btcusd/summary the high price was not larger than the low')
        self.assertTrue(priceData['low'] <= priceData['last'] <= priceData['high'], 'bitfinex/btcusd/summary the last price was not between high and low')
        self.assertTrue(type(priceData['change']['percentage']) == int or float, 'bitfinex/btcusd/summary change percentage was not a number')
        self.assertTrue(type(priceData['change']['absolute']) == int or float, 'bitfinex/btcusd/summary change absolute was not a number')
        self.assertGreater(jsonData['volume'], 0, 'bitfinex/btcusd/summary volume was not greater than zero')
        self.assertGreater(jsonData['volumeQuote'], 0, 'bitfinex/btcusd/summary volume quote was not greater than zero')

        self.assertGreater(allowData['cost'], 0, 'bitfinex/btcusd/summary allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, 'bitfinex/btcusd/summary allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", 'bitfinex/btcusd/summary upgrade message was incorrect')

    # Verify the bitfinex/ltcusd/summary endpoint
    def test_bitfinex_ltcusd_summary(self):
        resp = requests.get(url + bitfinex_ltcusd + '/summary', auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        priceData = resp.json()['result']['price']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, 'The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertGreaterEqual(priceData['high'], priceData['low'], 'bitfinex/ltcusd/summary the high price was not larger than the low')
        self.assertTrue(priceData['low'] <= priceData['last'] <= priceData['high'], 'bitfinex/ltcusd/summary the last price was not between high and low')
        self.assertTrue(type(priceData['change']['percentage']) == int or float, 'bitfinex/ltcusd/summary change percentage was not a number')
        self.assertTrue(type(priceData['change']['absolute']) == int or float, 'bitfinex/ltcusd/summary change absolute was not a number')
        self.assertGreater(jsonData['volume'], 0, 'bitfinex/ltcusd/summary volume was not greater than zero')
        self.assertGreater(jsonData['volumeQuote'], 0, 'bitfinex/ltcusd/summary volume quote was not greater than zero')

        self.assertGreater(allowData['cost'], 0, 'bitfinex/ltcusd/trades allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, 'bitfinex/ltcusd/trades allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", 'bitfinex/ltcusd/trades upgrade message was incorrect')

    # Verify the bitfinex/ltcbtc/summary endpoint
    def test_bitfinex_ltcbtc_summary(self):
        resp = requests.get(url + bitfinex_ltcbtc + '/summary', auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        priceData = resp.json()['result']['price']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, 'The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertGreaterEqual(priceData['high'], priceData['low'], 'bitfinex/ltcbtc/summary the high price was not larger than the low')
        self.assertTrue(priceData['low'] <= priceData['last'] <= priceData['high'], 'bitfinex/ltcbtc/summary the last price was not between high and low')
        self.assertTrue(type(priceData['change']['percentage']) == int or float, 'bitfinex/ltcbtc/summary change percentage was not a number')
        self.assertTrue(type(priceData['change']['absolute']) == int or float, 'bitfinex/ltcbtc/summary change absolute was not a number')
        self.assertGreater(jsonData['volume'], 0, 'bitfinex/ltcbtc/summary volume was not greater than zero')
        self.assertGreater(jsonData['volumeQuote'], 0, 'bitfinex/ltcbtc/summary volume quote was not greater than zero')

        self.assertGreater(allowData['cost'], 0, 'bitfinex/ltcbtc/summary allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, 'bitfinex/ltcbtc/summary allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", 'bitfinex/ltcbtc/summary upgrade message was incorrect')

    # Verify the bitfinex/ethusd/summary endpoint
    def test_bitfinex_ethusd_summary(self):
        resp = requests.get(url + bitfinex_ethusd + '/summary', auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        priceData = resp.json()['result']['price']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, 'The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertGreaterEqual(priceData['high'], priceData['low'], 'bitfinex/ethusd/summary the high price was not larger than the low')
        self.assertTrue(priceData['low'] <= priceData['last'] <= priceData['high'], 'bitfinex/ethusd/summary the last price was not between high and low')
        self.assertTrue(type(priceData['change']['percentage']) == int or float, 'bitfinex/ethusd/summary change percentage was not a number')
        self.assertTrue(type(priceData['change']['absolute']) == int or float, 'bitfinex/ethusd/summary change absolute was not a number')
        self.assertGreater(jsonData['volume'], 0, 'bitfinex/ethusd/summary volume was not greater than zero')
        self.assertGreater(jsonData['volumeQuote'], 0, 'bitfinex/ethusd/summary volume quote was not greater than zero')

        self.assertGreater(allowData['cost'], 0, 'bitfinex/ethusd/summary allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, 'bitfinex/ethusd/summary allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", 'bitfinex/ethusd/summary upgrade message was incorrect')

    # Verify the bitfinex/ethbtc/summary endpoint
    def test_bitfinex_ethbtc_summary(self):
        resp = requests.get(url + bitfinex_ethbtc + '/summary', auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        priceData = resp.json()['result']['price']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, 'The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertGreaterEqual(priceData['high'], priceData['low'], 'bitfinex/ethbtc/summary the high price was not larger than the low')
        self.assertTrue(priceData['low'] <= priceData['last'] <= priceData['high'], 'bitfinex/ethbtc/summary the last price was not between high and low')
        self.assertTrue(type(priceData['change']['percentage']) == int or float, 'bitfinex/ethbtc/summary change percentage was not a number')
        self.assertTrue(type(priceData['change']['absolute']) == int or float, 'bitfinex/ethbtc/summary change absolute was not a number')
        self.assertGreater(jsonData['volume'], 0, 'bitfinex/ethbtc/summary volume was not greater than zero')
        self.assertGreater(jsonData['volumeQuote'], 0, 'bitfinex/ethbtc/summary volume quote was not greater than zeroo')

        self.assertGreater(allowData['cost'], 0, 'bitfinex/ethbtc/summary allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, 'bitfinex/ethbtc/summary allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", 'bitfinex/ethbtc/summary upgrade message was incorrect')
