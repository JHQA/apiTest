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
options = {'limit': 5,'timeout':4}

# Verify https://api.cryptowat.ch/markets/:exchange/:pair/orderbook
class TestOrderbook(unittest.TestCase):

    # Verify the /bitfinex/btcusd/orderbook endpoint
    def test_bitfinex_btcusd_orderbook(self):
        resp = requests.get(url + bitfinex_btcusd +'/orderbook', auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["asks"][0]), '/bitfinex/btcusd/orderbook asks did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["asks"][1]), '/bitfinex/btcusd/orderbook asks did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["asks"][2]), '/bitfinex/btcusd/orderbook asks did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["asks"][3]), '/bitfinex/btcusd/orderbook asks did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["asks"][4]), '/bitfinex/btcusd/orderbook asks did not return a list with numbers')

        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["bids"][0]), '/bitfinex/btcusd/orderbook bids did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["bids"][1]), '/bitfinex/btcusd/orderbook bids did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["bids"][2]), '/bitfinex/btcusd/orderbook bids did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["bids"][3]), '/bitfinex/btcusd/orderbook bids did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["bids"][4]), '/bitfinex/btcusd/orderbook bids did not return a list with numbers')

        self.assertTrue(jsonData['seqNum'] == int or float, '/bitfinex/btcusd/orderbook seqNum was not a number')

        self.assertGreater(allowData['cost'], 0, '/bitfinex/btcusd/orderbook allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, '/bitfinex/btcusd/orderbook allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", '/bitfinex/btcusd/orderbook upgrade message was incorrect')

    # Verify the /bitfinex/ltcusd/orderbook endpoint
    def test_bitfinex_ltcusd_orderbook(self):
        resp = requests.get(url + bitfinex_ltcusd +'/orderbook', auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["asks"][0]), '/bitfinex/ltcusd/orderbook asks did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["asks"][1]), '/bitfinex/ltcusd/orderbook asks did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["asks"][2]), '/bitfinex/ltcusd/orderbook asks did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["asks"][3]), '/bitfinex/ltcusd/orderbook asks did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["asks"][4]), '/bitfinex/ltcusd/orderbook asks did not return a list with numbers')

        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["bids"][0]), '/bitfinex/ltcusd/orderbook bids did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["bids"][1]), '/bitfinex/ltcusd/orderbook bids did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["bids"][2]), '/bitfinex/ltcusd/orderbook bids did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["bids"][3]), '/bitfinex/ltcusd/orderbook bids did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["bids"][4]), '/bitfinex/ltcusd/orderbook bids did not return a list with numbers')

        self.assertTrue(jsonData['seqNum'] == int or float, '/bitfinex/ltcusd/orderbook seqNum was not a number')

        self.assertGreater(allowData['cost'], 0, '/bitfinex/ltcusd/orderbook allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, '/bitfinex/ltcusd/orderbook allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", '/bitfinex/ltcusd/orderbook upgrade message was incorrect')


    # Verify the /bitfinex/ltcbtc/orderbook endpoint
    def test_bitfinex_ltcbtc_orderbook(self):
        resp = requests.get(url + bitfinex_ltcbtc +'/orderbook', auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["asks"][0]), '/bitfinex/ltcbtc/orderbook asks did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["asks"][1]), '/bitfinex/ltcbtc/orderbook asks did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["asks"][2]), '/bitfinex/ltcbtc/orderbook asks did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["asks"][3]), '/bitfinex/ltcbtc/orderbook asks did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["asks"][4]), '/bitfinex/ltcbtc/orderbook asks did not return a list with numbers')

        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["bids"][0]), '/bitfinex/ltcbtc/orderbook bids did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["bids"][1]), '/bitfinex/ltcbtc/orderbook bids did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["bids"][2]), '/bitfinex/ltcbtc/orderbook bids did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["bids"][3]), '/bitfinex/ltcbtc/orderbook bids did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["bids"][4]), '/bitfinex/ltcbtc/orderbook bids did not return a list with numbers')

        self.assertTrue(jsonData['seqNum'] == int or float, '/bitfinex/ltcbtc/orderbook seqNum was not a number')

        self.assertGreater(allowData['cost'], 0, '/bitfinex/ltcbtc/orderbook allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, '/bitfinex/ltcbtc/orderbook allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", '/bitfinex/ltcbtc/orderbook upgrade message was incorrect')

    # Verify the /bitfinex/ethusd/orderbook endpoint
    def test_bitfinex_ethusd_orderbook(self):
        resp = requests.get(url + bitfinex_ethusd +'/orderbook', auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["asks"][0]), '/bitfinex/ethusd/orderbook asks did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["asks"][1]), '/bitfinex/ethusd/orderbook asks did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["asks"][2]), '/bitfinex/ethusd/orderbook asks did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["asks"][3]), '/bitfinex/ethusd/orderbook asks did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["asks"][4]), '/bitfinex/ethusd/orderbook asks did not return a list with numbers')

        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["bids"][0]), '/bitfinex/ethusd/orderbook bids did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["bids"][1]), '/bitfinex/ethusd/orderbook bids did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["bids"][2]), '/bitfinex/ethusd/orderbook bids did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["bids"][3]), '/bitfinex/ethusd/orderbook bids did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["bids"][4]), '/bitfinex/ethusd/orderbook bids did not return a list with numbers')

        self.assertTrue(jsonData['seqNum'] == int or float, '/bitfinex/ethusd/orderbook seqNum was not a number')

        self.assertGreater(allowData['cost'], 0, '/bitfinex/ethusd/orderbook allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, '/bitfinex/ethusd/orderbook allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", '/bitfinex/ethusd/orderbook upgrade message was incorrect')

    # Verify the /bitfinex/ethbtc/orderbook endpoint
    def test_bitfinex_ethbtc_orderbook(self):
        resp = requests.get(url + bitfinex_ethbtc +'/orderbook', auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["asks"][0]), '/bitfinex/ethbtc/orderbook asks did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["asks"][1]), '/bitfinex/ethbtc/orderbook asks did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["asks"][2]), '/bitfinex/ethbtc/orderbook asks did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["asks"][3]), '/bitfinex/ethbtc/orderbook asks did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["asks"][4]), '/bitfinex/ethbtc/orderbook asks did not return a list with numbers')

        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["bids"][0]), '/bitfinex/ethbtc/orderbook bids did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["bids"][1]), '/bitfinex/ethbtc/orderbook bids did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["bids"][2]), '/bitfinex/ethbtc/orderbook bids did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["bids"][3]), '/bitfinex/ethbtc/orderbook bids did not return a list with numbers')
        self.assertTrue(all(isinstance(item, (int, float)) for item in jsonData["bids"][4]), '/bitfinex/ethbtc/orderbook bids did not return a list with numbers')

        self.assertTrue(jsonData['seqNum'] == int or float, '/bitfinex/ethbtc/orderbook seqNum was not a number')

        self.assertGreater(allowData['cost'], 0, '/bitfinex/ethbtc/orderbook allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, '/bitfinex/ethbtc/orderbook allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", '/bitfinex/ethbtc/orderbook upgrade message was incorrect')

