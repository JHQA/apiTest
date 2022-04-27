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

# Verify https://api.cryptowat.ch/markets/:exchange/:pair/orderbook/liquidity
class TestOrderbookLiquidity(unittest.TestCase):

    # Verify the /bitfinex/btcusd/orderbook/liquidity endpoint
    def test_bitfinex_btcusd_orderbook_liquidity(self):
        resp = requests.get(url + bitfinex_btcusd +'/orderbook/liquidity', auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertTrue((type(jsonData["bid"]['base']['100']) == int or float), '/bitfinex/btcusd/orderbook/liquidity bid base 100 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['150']) == int or float), '/bitfinex/btcusd/orderbook/liquidity bid base 150 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['200']) == int or float), '/bitfinex/btcusd/orderbook/liquidity bid base 200 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['25']) == int or float), '/bitfinex/btcusd/orderbook/liquidity bid base 25 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['250']) == int or float), '/bitfinex/btcusd/orderbook/liquidity bid base 250 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['300']) == int or float), '/bitfinex/btcusd/orderbook/liquidity bid base 300 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['400']) == int or float), '/bitfinex/btcusd/orderbook/liquidity bid base 400 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['50']) == int or float), '/bitfinex/btcusd/orderbook/liquidity bid base 50 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['500']) == int or float), '/bitfinex/btcusd/orderbook/liquidity bid base 500 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['75']) == int or float), '/bitfinex/btcusd/orderbook/liquidity bid base 75 did not return a numbers')

        self.assertTrue((type(jsonData["bid"]['quote']['100']) == int or float), '/bitfinex/btcusd/orderbook/liquidity bid quote 100 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['150']) == int or float), '/bitfinex/btcusd/orderbook/liquidity bid quote 150 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['200']) == int or float), '/bitfinex/btcusd/orderbook/liquidity bid quote 200 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['25']) == int or float), '/bitfinex/btcusd/orderbook/liquidity bid quote 25 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['250']) == int or float), '/bitfinex/btcusd/orderbook/liquidity bid quote 250 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['300']) == int or float), '/bitfinex/btcusd/orderbook/liquidity bid quote 300 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['400']) == int or float), '/bitfinex/btcusd/orderbook/liquidity bid quote 400 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['50']) == int or float), '/bitfinex/btcusd/orderbook/liquidity bid quote 50 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['500']) == int or float), '/bitfinex/btcusd/orderbook/liquidity bid quote 500 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['75']) == int or float), '/bitfinex/btcusd/orderbook/liquidity bid quote 75 did not return a numbers')

        self.assertTrue((type(jsonData["ask"]['base']['100']) == int or float), '/bitfinex/btcusd/orderbook/liquidity ask base 100 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['150']) == int or float), '/bitfinex/btcusd/orderbook/liquidity ask base 150 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['200']) == int or float), '/bitfinex/btcusd/orderbook/liquidity ask base 200 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['25']) == int or float), '/bitfinex/btcusd/orderbook/liquidity ask base 25 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['250']) == int or float), '/bitfinex/btcusd/orderbook/liquidity ask base 250 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['300']) == int or float), '/bitfinex/btcusd/orderbook/liquidity ask base 300 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['400']) == int or float), '/bitfinex/btcusd/orderbook/liquidity ask base 400 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['50']) == int or float), '/bitfinex/btcusd/orderbook/liquidity ask base 50 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['500']) == int or float), '/bitfinex/btcusd/orderbook/liquidity ask base 500 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['75']) == int or float), '/bitfinex/btcusd/orderbook/liquidity ask base 75 did not return a numbers')

        self.assertTrue((type(jsonData["ask"]['quote']['100']) == int or float), '/bitfinex/btcusd/orderbook/liquidity ask quote 100 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['150']) == int or float), '/bitfinex/btcusd/orderbook/liquidity ask quote 150 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['200']) == int or float), '/bitfinex/btcusd/orderbook/liquidity ask quote 200 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['25']) == int or float), '/bitfinex/btcusd/orderbook/liquidity ask quote 25 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['250']) == int or float), '/bitfinex/btcusd/orderbook/liquidity ask quote 250 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['300']) == int or float), '/bitfinex/btcusd/orderbook/liquidity ask quote 300 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['400']) == int or float), '/bitfinex/btcusd/orderbook/liquidity ask quote 400 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['50']) == int or float), '/bitfinex/btcusd/orderbook/liquidity ask quote 50 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['500']) == int or float), '/bitfinex/btcusd/orderbook/liquidity ask quote 500 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['75']) == int or float), '/bitfinex/btcusd/orderbook/liquidity ask quote 75 did not return a numbers')

        self.assertGreater(allowData['cost'], 0, '/bitfinex/btcusd/orderbook/liquidity allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, '/bitfinex/btcusd/orderbook/liquidity allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", '/bitfinex/btcusd/orderbook/liquidity upgrade message was incorrect')

    # Verify the /bitfinex/ltcusd/orderbook/liquidity endpoint
    def test_bitfinex_ltcusd_orderbook_liquidity(self):
        resp = requests.get(url + bitfinex_ltcusd +'/orderbook/liquidity', auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertTrue((type(jsonData["bid"]['base']['100']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity bid base 100 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['150']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity bid base 150 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['200']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity bid base 200 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['25']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity bid base 25 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['250']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity bid base 250 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['300']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity bid base 300 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['400']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity bid base 400 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['50']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity bid base 50 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['500']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity bid base 500 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['75']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity bid base 75 did not return a numbers')

        self.assertTrue((type(jsonData["bid"]['quote']['100']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity bid quote 100 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['150']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity bid quote 150 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['200']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity bid quote 200 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['25']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity bid quote 25 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['250']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity bid quote 250 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['300']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity bid quote 300 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['400']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity bid quote 400 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['50']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity bid quote 50 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['500']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity bid quote 500 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['75']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity bid quote 75 did not return a numbers')

        self.assertTrue((type(jsonData["ask"]['base']['100']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity ask base 100 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['150']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity ask base 150 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['200']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity ask base 200 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['25']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity ask base 25 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['250']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity ask base 250 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['300']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity ask base 300 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['400']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity ask base 400 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['50']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity ask base 50 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['500']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity ask base 500 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['75']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity ask base 75 did not return a numbers')

        self.assertTrue((type(jsonData["ask"]['quote']['100']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity ask quote 100 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['150']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity ask quote 150 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['200']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity ask quote 200 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['25']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity ask quote 25 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['250']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity ask quote 250 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['300']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity ask quote 300 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['400']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity ask quote 400 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['50']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity ask quote 50 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['500']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity ask quote 500 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['75']) == int or float), '/bitfinex/ltcusd/orderbook/liquidity ask quote 75 did not return a numbers')

        self.assertGreater(allowData['cost'], 0, '/bitfinex/ltcusd/orderbook/liquidity allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, '/bitfinex/ltcusd/orderbook/liquidity allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", '/bitfinex/ltcusd/orderbook/liquidity upgrade message was incorrect')


    # Verify the /bitfinex/ltcbtc/orderbook/liquidity endpoint
    def test_bitfinex_ltcbtc_orderbook_liquidity_liquidity(self):
        resp = requests.get(url + bitfinex_ltcbtc +'/orderbook/liquidity', auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertTrue((type(jsonData["bid"]['base']['100']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity bid base 100 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['150']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity bid base 150 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['200']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity bid base 200 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['25']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity bid base 25 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['250']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity bid base 250 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['300']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity bid base 300 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['400']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity bid base 400 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['50']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity bid base 50 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['500']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity bid base 500 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['75']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity bid base 75 did not return a numbers')

        self.assertTrue((type(jsonData["bid"]['quote']['100']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity bid quote 100 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['150']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity bid quote 150 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['200']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity bid quote 200 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['25']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity bid quote 25 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['250']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity bid quote 250 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['300']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity bid quote 300 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['400']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity bid quote 400 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['50']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity bid quote 50 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['500']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity bid quote 500 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['75']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity bid quote 75 did not return a numbers')

        self.assertTrue((type(jsonData["ask"]['base']['100']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity ask base 100 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['150']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity ask base 150 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['200']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity ask base 200 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['25']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity ask base 25 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['250']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity ask base 250 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['300']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity ask base 300 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['400']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity ask base 400 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['50']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity ask base 50 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['500']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity ask base 500 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['75']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity ask base 75 did not return a numbers')

        self.assertTrue((type(jsonData["ask"]['quote']['100']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity ask quote 100 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['150']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity ask quote 150 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['200']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity ask quote 200 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['25']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity ask quote 25 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['250']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity ask quote 250 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['300']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity ask quote 300 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['400']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity ask quote 400 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['50']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity ask quote 50 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['500']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity ask quote 500 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['75']) == int or float), '/bitfinex/ltcbtc/orderbook/liquidity ask quote 75 did not return a numbers')

        self.assertGreater(allowData['cost'], 0, '/bitfinex/ltcbtc/orderbook/liquidity allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, '/bitfinex/ltcbtc/orderbook/liquidity allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", '/bitfinex/ltcbtc/orderbook/liquidity upgrade message was incorrect')

    # Verify the /bitfinex/ethusd/orderbook/liquidity endpoint
    def test_bitfinex_ethusd_orderbook_liquidity(self):
        resp = requests.get(url + bitfinex_ethusd +'/orderbook/liquidity', auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertTrue((type(jsonData["bid"]['base']['100']) == int or float), '/bitfinex/ethusd/orderbook/liquidity bid base 100 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['150']) == int or float), '/bitfinex/ethusd/orderbook/liquidity bid base 150 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['200']) == int or float), '/bitfinex/ethusd/orderbook/liquidity bid base 200 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['25']) == int or float), '/bitfinex/ethusd/orderbook/liquidity bid base 25 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['250']) == int or float), '/bitfinex/ethusd/orderbook/liquidity bid base 250 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['300']) == int or float), '/bitfinex/ethusd/orderbook/liquidity bid base 300 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['400']) == int or float), '/bitfinex/ethusd/orderbook/liquidity bid base 400 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['50']) == int or float), '/bitfinex/ethusd/orderbook/liquidity bid base 50 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['500']) == int or float), '/bitfinex/ethusd/orderbook/liquidity bid base 500 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['75']) == int or float), '/bitfinex/ethusd/orderbook/liquidity bid base 75 did not return a numbers')

        self.assertTrue((type(jsonData["bid"]['quote']['100']) == int or float), '/bitfinex/ethusd/orderbook/liquidity bid quote 100 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['150']) == int or float), '/bitfinex/ethusd/orderbook/liquidity bid quote 150 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['200']) == int or float), '/bitfinex/ethusd/orderbook/liquidity bid quote 200 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['25']) == int or float), '/bitfinex/ethusd/orderbook/liquidity bid quote 25 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['250']) == int or float), '/bitfinex/ethusd/orderbook/liquidity bid quote 250 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['300']) == int or float), '/bitfinex/ethusd/orderbook/liquidity bid quote 300 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['400']) == int or float), '/bitfinex/ethusd/orderbook/liquidity bid quote 400 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['50']) == int or float), '/bitfinex/ethusd/orderbook/liquidity bid quote 50 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['500']) == int or float), '/bitfinex/ethusd/orderbook/liquidity bid quote 500 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['75']) == int or float), '/bitfinex/ethusd/orderbook/liquidity bid quote 75 did not return a numbers')

        self.assertTrue((type(jsonData["ask"]['base']['100']) == int or float), '/bitfinex/ethusd/orderbook/liquidity ask base 100 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['150']) == int or float), '/bitfinex/ethusd/orderbook/liquidity ask base 150 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['200']) == int or float), '/bitfinex/ethusd/orderbook/liquidity ask base 200 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['25']) == int or float), '/bitfinex/ethusd/orderbook/liquidity ask base 25 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['250']) == int or float), '/bitfinex/ethusd/orderbook/liquidity ask base 250 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['300']) == int or float), '/bitfinex/ethusd/orderbook/liquidity ask base 300 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['400']) == int or float), '/bitfinex/ethusd/orderbook/liquidity ask base 400 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['50']) == int or float), '/bitfinex/ethusd/orderbook/liquidity ask base 50 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['500']) == int or float), '/bitfinex/ethusd/orderbook/liquidity ask base 500 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['75']) == int or float), '/bitfinex/ethusd/orderbook/liquidity ask base 75 did not return a numbers')

        self.assertTrue((type(jsonData["ask"]['quote']['100']) == int or float), '/bitfinex/ethusd/orderbook/liquidity ask quote 100 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['150']) == int or float), '/bitfinex/ethusd/orderbook/liquidity ask quote 150 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['200']) == int or float), '/bitfinex/ethusd/orderbook/liquidity ask quote 200 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['25']) == int or float), '/bitfinex/ethusd/orderbook/liquidity ask quote 25 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['250']) == int or float), '/bitfinex/ethusd/orderbook/liquidity ask quote 250 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['300']) == int or float), '/bitfinex/ethusd/orderbook/liquidity ask quote 300 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['400']) == int or float), '/bitfinex/ethusd/orderbook/liquidity ask quote 400 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['50']) == int or float), '/bitfinex/ethusd/orderbook/liquidity ask quote 50 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['500']) == int or float), '/bitfinex/ethusd/orderbook/liquidity ask quote 500 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['75']) == int or float), '/bitfinex/ethusd/orderbook/liquidity ask quote 75 did not return a numbers')

        self.assertGreater(allowData['cost'], 0, '/bitfinex/ethusd/orderbook/liquidity allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, '/bitfinex/ethusd/orderbook/liquidity allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", '/bitfinex/ltcbtc/orderbook/liquidity upgrade message was incorrect')
    
    # Verify the /bitfinex/ethbtc/orderbook/liquidity endpoint
    def test_bitfinex_ethbtc_orderbook_liquidity(self):
        resp = requests.get(url + bitfinex_ethbtc +'/orderbook/liquidity', auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertTrue((type(jsonData["bid"]['base']['100']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity bid base 100 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['150']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity bid base 150 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['200']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity bid base 200 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['25']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity bid base 25 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['250']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity bid base 250 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['300']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity bid base 300 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['400']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity bid base 400 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['50']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity bid base 50 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['500']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity bid base 500 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['base']['75']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity bid base 75 did not return a numbers')

        self.assertTrue((type(jsonData["bid"]['quote']['100']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity bid quote 100 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['150']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity bid quote 150 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['200']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity bid quote 200 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['25']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity bid quote 25 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['250']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity bid quote 250 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['300']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity bid quote 300 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['400']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity bid quote 400 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['50']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity bid quote 50 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['500']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity bid quote 500 did not return a numbers')
        self.assertTrue((type(jsonData["bid"]['quote']['75']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity bid quote 75 did not return a numbers')

        self.assertTrue((type(jsonData["ask"]['base']['100']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity ask base 100 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['150']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity ask base 150 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['200']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity ask base 200 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['25']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity ask base 25 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['250']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity ask base 250 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['300']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity ask base 300 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['400']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity ask base 400 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['50']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity ask base 50 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['500']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity ask base 500 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['base']['75']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity ask base 75 did not return a numbers')

        self.assertTrue((type(jsonData["ask"]['quote']['100']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity ask quote 100 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['150']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity ask quote 150 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['200']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity ask quote 200 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['25']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity ask quote 25 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['250']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity ask quote 250 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['300']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity ask quote 300 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['400']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity ask quote 400 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['50']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity ask quote 50 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['500']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity ask quote 500 did not return a numbers')
        self.assertTrue((type(jsonData["ask"]['quote']['75']) == int or float), '/bitfinex/ethbtc/orderbook/liquidity ask quote 75 did not return a numbers')

        self.assertGreater(allowData['cost'], 0, '/bitfinex/ethbtc/orderbook/liquidity allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, '/bitfinex/ethbtc/orderbook/liquidity allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", '/bitfinex/ethbtc/orderbook/liquidity upgrade message was incorrect')
