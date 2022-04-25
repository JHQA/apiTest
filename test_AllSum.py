import unittest
import requests

# Credentials
email = ''
apiKey = ''

# API point and options
url = 'https://api.cryptowat.ch/markets/summaries'
options = {'limit': 5, 'timeout':4}

resp = requests.get(url, auth=(email, apiKey), params= options)
jsonData = resp.json()['result']
allowData = resp.json()['allowance']
cursorData = resp.json()['cursor']

class TestAllSum(unittest.TestCase):

    # Verify the markets/summaries api status code is 200
    def test_status(self):
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears /markets')
    
    # Verify the headers content-type is application/json
    def test_headers(self):
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content-type appears /markets')

    # Verify bitfinex/btcusd summary has the correct info
    def test_btcusd(self):
        self.assertEqual(resp.status_code, 200, 'The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertGreaterEqual(jsonData['bitfinex:btcusd']['price']['high'], jsonData['bitfinex:btcusd']['price']['low'], 'summaries bitfinex/btcusd the high price was not larger than the low')
        self.assertTrue(jsonData['bitfinex:btcusd']['price']['low'] <= jsonData['bitfinex:btcusd']['price']['last'] <= jsonData['bitfinex:btcusd']['price']['high'], 'summaries bitfinex/btcusd the last price was not between high and low')
        self.assertTrue(type(jsonData['bitfinex:btcusd']['price']['change']['percentage']) == int or float, 'summaries bitfinex/btcusd change percentage was not a number')
        self.assertTrue(type(jsonData['bitfinex:btcusd']['price']['change']['absolute']) == int or float, 'summaries bitfinex/btcusd change absolute was not a number')
        self.assertGreater(jsonData['bitfinex:btcusd']['volume'], 0, 'summaries bitfinex/btcusd volume was not greater than zero')
        self.assertGreater(jsonData['bitfinex:btcusd']['volumeQuote'], 0, 'summaries bitfinex/btcusd volume quote was not greater than zero')

    # Verify ethbtc has the correct info
    def test_ethbtc(self):
        self.assertEqual(resp.status_code, 200, 'The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertGreaterEqual(jsonData['bitfinex:ethbtc']['price']['high'], jsonData['bitfinex:ethbtc']['price']['low'], 'summaries bitfinex/ethbtc the high price was not larger than the low')
        self.assertTrue(jsonData['bitfinex:ethbtc']['price']['low'] <= jsonData['bitfinex:ethbtc']['price']['last'] <= jsonData['bitfinex:ethbtc']['price']['high'], 'summaries bitfinex/ethbtc the last price was not between high and low')
        self.assertTrue(type(jsonData['bitfinex:ethbtc']['price']['change']['percentage']) == int or float, 'summaries bitfinex/ethbtc change percentage was not a numbe')
        self.assertTrue(type(jsonData['bitfinex:ethbtc']['price']['change']['absolute']) == int or float, 'summaries bitfinex/ethbtc change absolute was not a number')
        self.assertGreater(jsonData['bitfinex:ethbtc']['volume'], 0, 'summaries bitfinex/ethbtc volume was not greater than zero')
        self.assertGreater(jsonData['bitfinex:ethbtc']['volumeQuote'], 0, 'summaries bitfinex/ethbtc volume was not greater than zero')

    # Verify ethusd has the correct info
    def test_ethusd(self):
        self.assertEqual(resp.status_code, 200, 'The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertGreaterEqual(jsonData['bitfinex:ethusd']['price']['high'], jsonData['bitfinex:ethusd']['price']['low'], 'summaries bitfinex/ethusd the high price was not larger than the low')
        self.assertTrue(jsonData['bitfinex:ethusd']['price']['low'] <= jsonData['bitfinex:ethusd']['price']['last'] <= jsonData['bitfinex:ethusd']['price']['high'], 'summaries bitfinex/ethusd the last price was not between high and low')
        self.assertTrue(type(jsonData['bitfinex:ethusd']['price']['change']['percentage']) == int or float, 'summaries bitfinex/ethusd change percentage was not a numbe')
        self.assertTrue(type(jsonData['bitfinex:ethusd']['price']['change']['absolute']) == int or float, 'summaries bitfinex/ethusd change absolute was not a number')
        self.assertGreater(jsonData['bitfinex:ethusd']['volume'], 0, 'summaries bitfinex/ethusd volume was not greater than zero')
        self.assertGreater(jsonData['bitfinex:ethusd']['volumeQuote'], 0, 'summaries bitfinex/ethusd volume was not greater than zero')

    # Verify ltcbtc has the correct info
    def test_ltcbtc(self):
        self.assertEqual(resp.status_code, 200, 'The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertGreaterEqual(jsonData['bitfinex:ltcbtc']['price']['high'], jsonData['bitfinex:ltcbtc']['price']['low'], 'summaries bitfinex/ltcbtc the high price was not larger than the low')
        self.assertTrue(jsonData['bitfinex:ltcbtc']['price']['low'] <= jsonData['bitfinex:ltcbtc']['price']['last'] <= jsonData['bitfinex:ltcbtc']['price']['high'], 'summaries bitfinex/ltcbtc the last price was not between high and low')
        self.assertTrue(type(jsonData['bitfinex:ltcbtc']['price']['change']['percentage']) == int or float, 'summaries bitfinex/ltcbtc change percentage was not a numbe')
        self.assertTrue(type(jsonData['bitfinex:ltcbtc']['price']['change']['absolute']) == int or float, 'summaries bitfinex/ltcbtc change absolute was not a number')
        self.assertGreater(jsonData['bitfinex:ltcbtc']['volume'], 0, 'summaries bitfinex/ltcbtc volume was not greater than zero')
        self.assertGreater(jsonData['bitfinex:ltcbtc']['volumeQuote'], 0, 'summaries bitfinex/ltcbtc volume was not greater than zero')

    # Verify ltcusd has the correct info
    def test_ltcusd(self):
        self.assertEqual(resp.status_code, 200, 'The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertGreaterEqual(jsonData['bitfinex:ltcusd']['price']['high'], jsonData['bitfinex:ltcusd']['price']['low'], 'summaries bitfinex/ltcusd the high price was not larger than the low')
        self.assertTrue(jsonData['bitfinex:ltcusd']['price']['low'] <= jsonData['bitfinex:ltcusd']['price']['last'] <= jsonData['bitfinex:ltcusd']['price']['high'], 'summaries bitfinex/ltcusd the last price was not between high and low')
        self.assertTrue(type(jsonData['bitfinex:ltcusd']['price']['change']['percentage']) == int or float, 'summaries bitfinex/ltcusd change percentage was not a numbe')
        self.assertTrue(type(jsonData['bitfinex:ltcusd']['price']['change']['absolute']) == int or float, 'summaries bitfinex/ltcusd price absolute was not a number')
        self.assertGreater(jsonData['bitfinex:ltcusd']['volume'], 0, 'summaries bitfinex/ltcusd volume was not greater than zero')
        self.assertGreater(jsonData['bitfinex:ltcusd']['volumeQuote'], 0, 'summaries bitfinex/ltcusd volume was not greater than zero')

    # Verify cursor data
    def test_cursor(self):
        self.assertTrue(cursorData['last'], '/markets/summaries cursor "last" should not be empty')
        self.assertTrue(cursorData['hasMore'], '/markets/summaries cursor "hasMore" was not true')

    # Verify allowance data
    def test_allowance(self):
        self.assertGreater(allowData['cost'], 0, '/markets/summaries allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, '/markets/summaries allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", '/markets/summaries allowance upgrade message was incorrect')
