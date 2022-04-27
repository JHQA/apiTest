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

# Amounts
typeInt = '?amount=50'
typeFloat = '?amount=12.5'

# Verify https://api.cryptowat.ch/markets/:exchange/:pair/orderbook/calculator
class TestOrderbookCalculator(unittest.TestCase):
    
    # Verify the /bitfinex/btcusd/orderbook/calculator endpoint amount as an integer 
    def test_bitfinex_btcusd_orderbook_int(self):
        resp = requests.get(url + bitfinex_btcusd +'/orderbook/calculator'+ typeInt, auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertTrue((type(jsonData['buy']['avgPrice']) == int or float), '/bitfinex/btcusd/orderbook/calculator buy avgPrice amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['avgDelta']) == int or float), '/bitfinex/btcusd/orderbook/calculator buy avgDelta amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['avgDeltaBps']) == int or float), '/bitfinex/btcusd/orderbook/calculator buy avgDeltaBps amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['reachPrice']) == int or float), '/bitfinex/btcusd/orderbook/calculator buy reachPrice amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['reachDelta']) == int or float), '/bitfinex/btcusd/orderbook/calculator buy reachDelta amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['reachDeltaBps']) == int or float), '/bitfinex/btcusd/orderbook/calculator buy reachDeltaBps amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['spend']) == int or float), '/bitfinex/btcusd/orderbook/calculator buy spend amount' +typeInt+ ' did not return a numbers')

        self.assertTrue((type(jsonData['sell']['avgPrice']) == int or float), '/bitfinex/btcusd/orderbook/calculator sell avgPrice amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['avgDelta']) == int or float), '/bitfinex/btcusd/orderbook/calculator sell avgDelta amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['avgDeltaBps']) == int or float), '/bitfinex/btcusd/orderbook/calculator sell avgDeltaBps amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['reachPrice']) == int or float), '/bitfinex/btcusd/orderbook/calculator sell reachPrice amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['reachDelta']) == int or float), '/bitfinex/btcusd/orderbook/calculator sell reachDelta amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['reachDeltaBps']) == int or float), '/bitfinex/btcusd/orderbook/calculator sell reachDeltaBps amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['receive']) == int or float), '/bitfinex/btcusd/orderbook/calculator sell spend amount' +typeInt+ ' did not return a numbers')

        self.assertGreater(allowData['cost'], 0, '/bitfinex/btcusd/orderbook/calculator allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, '/bitfinex/btcusd/orderbook/calculator allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", '/bitfinex/btcusd/orderbook/calculator upgrade message was incorrect')

    # Verify the /bitfinex/btcusd/orderbook/calculator endpoint amount as a float
    def test_bitfinex_btcusd_orderbook_float(self):
        resp = requests.get(url + bitfinex_btcusd +'/orderbook/calculator'+ typeFloat, auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertTrue((type(jsonData['buy']['avgPrice']) == int or float), '/bitfinex/btcusd/orderbook/calculator buy avgPrice amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['avgDelta']) == int or float), '/bitfinex/btcusd/orderbook/calculator buy avgDelta amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['avgDeltaBps']) == int or float), '/bitfinex/btcusd/orderbook/calculator buy avgDeltaBps amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['reachPrice']) == int or float), '/bitfinex/btcusd/orderbook/calculator buy reachPrice amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['reachDelta']) == int or float), '/bitfinex/btcusd/orderbook/calculator buy reachDelta amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['reachDeltaBps']) == int or float), '/bitfinex/btcusd/orderbook/calculator buy reachDeltaBps amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['spend']) == int or float), '/bitfinex/btcusd/orderbook/calculator buy spend amount' +typeFloat+ ' did not return a numbers')

        self.assertTrue((type(jsonData['sell']['avgPrice']) == int or float), '/bitfinex/btcusd/orderbook/calculator sell avgPrice amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['avgDelta']) == int or float), '/bitfinex/btcusd/orderbook/calculator sell avgDelta amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['avgDeltaBps']) == int or float), '/bitfinex/btcusd/orderbook/calculator sell avgDeltaBps amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['reachPrice']) == int or float), '/bitfinex/btcusd/orderbook/calculator sell reachPrice amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['reachDelta']) == int or float), '/bitfinex/btcusd/orderbook/calculator sell reachDelta amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['reachDeltaBps']) == int or float), '/bitfinex/btcusd/orderbook/calculator sell reachDeltaBps amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['receive']) == int or float), '/bitfinex/btcusd/orderbook/calculator sell spend amount' +typeFloat+ ' did not return a numbers')

        self.assertGreater(allowData['cost'], 0, '/bitfinex/btcusd/orderbook/calculator allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, '/bitfinex/btcusd/orderbook/calculator allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", '/bitfinex/btcusd/orderbook/calculator upgrade message was incorrect')

    # Verify the /bitfinex/ltcusd/orderbook/calculator endpoint amount as an integer 
    def test_bitfinex_ltcusd_orderbook_int(self):
        resp = requests.get(url + bitfinex_ltcusd +'/orderbook/calculator'+ typeInt, auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertTrue((type(jsonData['buy']['avgPrice']) == int or float), '/bitfinex/ltcusd/orderbook/calculator buy avgPrice amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['avgDelta']) == int or float), '/bitfinex/ltcusd/orderbook/calculator buy avgDelta amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['avgDeltaBps']) == int or float), '/bitfinex/ltcusd/orderbook/calculator buy avgDeltaBps amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['reachPrice']) == int or float), '/bitfinex/ltcusd/orderbook/calculator buy reachPrice amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['reachDelta']) == int or float), '/bitfinex/ltcusd/orderbook/calculator buy reachDelta amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['reachDeltaBps']) == int or float), '/bitfinex/ltcusd/orderbook/calculator buy reachDeltaBps amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['spend']) == int or float), '/bitfinex/ltcusd/orderbook/calculator buy spend amount' +typeInt+ ' did not return a numbers')

        self.assertTrue((type(jsonData['sell']['avgPrice']) == int or float), '/bitfinex/ltcusd/orderbook/calculator sell avgPrice amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['avgDelta']) == int or float), '/bitfinex/ltcusd/orderbook/calculator sell avgDelta amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['avgDeltaBps']) == int or float), '/bitfinex/ltcusd/orderbook/calculator sell avgDeltaBps amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['reachPrice']) == int or float), '/bitfinex/ltcusd/orderbook/calculator sell reachPrice amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['reachDelta']) == int or float), '/bitfinex/ltcusd/orderbook/calculator sell reachDelta amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['reachDeltaBps']) == int or float), '/bitfinex/ltcusd/orderbook/calculator sell reachDeltaBps amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['receive']) == int or float), '/bitfinex/ltcusd/orderbook/calculator sell spend amount' +typeInt+ ' did not return a numbers')

        self.assertGreater(allowData['cost'], 0, '/bitfinex/ltcusd/orderbook/calculator allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, '/bitfinex/ltcusd/orderbook/calculator allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", '/bitfinex/ltcusd/orderbook/calculator upgrade message was incorrect')

    # Verify the /bitfinex/ltcusd/orderbook/calculator endpoint amount as a float
    def test_bitfinex_ltcusd_orderbook_float(self):
        resp = requests.get(url + bitfinex_ltcusd +'/orderbook/calculator'+ typeFloat, auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertTrue((type(jsonData['buy']['avgPrice']) == int or float), '/bitfinex/ltcusd/orderbook/calculator buy avgPrice amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['avgDelta']) == int or float), '/bitfinex/ltcusd/orderbook/calculator buy avgDelta amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['avgDeltaBps']) == int or float), '/bitfinex/ltcusd/orderbook/calculator buy avgDeltaBps amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['reachPrice']) == int or float), '/bitfinex/ltcusd/orderbook/calculator buy reachPrice amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['reachDelta']) == int or float), '/bitfinex/ltcusd/orderbook/calculator buy reachDelta amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['reachDeltaBps']) == int or float), '/bitfinex/ltcusd/orderbook/calculator buy reachDeltaBps amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['spend']) == int or float), '/bitfinex/ltcusd/orderbook/calculator buy spend amount' +typeFloat+ ' did not return a numbers')

        self.assertTrue((type(jsonData['sell']['avgPrice']) == int or float), '/bitfinex/ltcusd/orderbook/calculator sell avgPrice amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['avgDelta']) == int or float), '/bitfinex/ltcusd/orderbook/calculator sell avgDelta amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['avgDeltaBps']) == int or float), '/bitfinex/ltcusd/orderbook/calculator sell avgDeltaBps amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['reachPrice']) == int or float), '/bitfinex/ltcusd/orderbook/calculator sell reachPrice amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['reachDelta']) == int or float), '/bitfinex/ltcusd/orderbook/calculator sell reachDelta amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['reachDeltaBps']) == int or float), '/bitfinex/ltcusd/orderbook/calculator sell reachDeltaBps amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['receive']) == int or float), '/bitfinex/ltcusd/orderbook/calculator sell spend amount' +typeFloat+ ' did not return a numbers')

        self.assertGreater(allowData['cost'], 0, '/bitfinex/ltcusd/orderbook/calculator allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, '/bitfinex/ltcusd/orderbook/calculator allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", '/bitfinex/ltcusd/orderbook/calculator upgrade message was incorrect')

    # Verify the /bitfinex/ltcbtc/orderbook/calculator endpoint amount as an integer 
    def test_bitfinex_ltcbtc_orderbook_int(self):
        resp = requests.get(url + bitfinex_ltcbtc +'/orderbook/calculator'+ typeInt, auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertTrue((type(jsonData['buy']['avgPrice']) == int or float), '/bitfinex/ltcbtc/orderbook/calculator buy avgPrice amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['avgDelta']) == int or float), '/bitfinex/ltcbtc/orderbook/calculator buy avgDelta amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['avgDeltaBps']) == int or float), '/bitfinex/ltcbtc/orderbook/calculator buy avgDeltaBps amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['reachPrice']) == int or float), '/bitfinex/ltcbtc/orderbook/calculator buy reachPrice amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['reachDelta']) == int or float), '/bitfinex/ltcbtc/orderbook/calculator buy reachDelta amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['reachDeltaBps']) == int or float), '/bitfinex/ltcbtc/orderbook/calculator buy reachDeltaBps amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['spend']) == int or float), '/bitfinex/ltcbtc/orderbook/calculator buy spend amount' +typeInt+ ' did not return a numbers')

        self.assertTrue((type(jsonData['sell']['avgPrice']) == int or float), '/bitfinex/ltcbtc/orderbook/calculator sell avgPrice amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['avgDelta']) == int or float), '/bitfinex/ltcbtc/orderbook/calculator sell avgDelta amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['avgDeltaBps']) == int or float), '/bitfinex/ltcbtc/orderbook/calculator sell avgDeltaBps amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['reachPrice']) == int or float), '/bitfinex/ltcbtc/orderbook/calculator sell reachPrice amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['reachDelta']) == int or float), '/bitfinex/ltcbtc/orderbook/calculator sell reachDelta amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['reachDeltaBps']) == int or float), '/bitfinex/ltcbtc/orderbook/calculator sell reachDeltaBps amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['receive']) == int or float), '/bitfinex/ltcbtc/orderbook/calculator sell spend amount' +typeInt+ ' did not return a numbers')

        self.assertGreater(allowData['cost'], 0, '/bitfinex/ltcbtc/orderbook/calculator allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, '/bitfinex/ltcbtc/orderbook/calculator allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", '/bitfinex/ltcbtc/orderbook/calculator upgrade message was incorrect')

    # Verify the /bitfinex/ltcbtc/orderbook/calculator endpoint amount as a float
    def test_bitfinex_ltcbtc_orderbook_float(self):
        resp = requests.get(url + bitfinex_ltcbtc +'/orderbook/calculator'+ typeFloat, auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertTrue((type(jsonData['buy']['avgPrice']) == int or float), '/bitfinex/ltcbtc/orderbook/calculator buy avgPrice amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['avgDelta']) == int or float), '/bitfinex/ltcbtc/orderbook/calculator buy avgDelta amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['avgDeltaBps']) == int or float), '/bitfinex/ltcbtc/orderbook/calculator buy avgDeltaBps amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['reachPrice']) == int or float), '/bitfinex/ltcbtc/orderbook/calculator buy reachPrice amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['reachDelta']) == int or float), '/bitfinex/ltcbtc/orderbook/calculator buy reachDelta amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['reachDeltaBps']) == int or float), '/bitfinex/ltcbtc/orderbook/calculator buy reachDeltaBps amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['spend']) == int or float), '/bitfinex/ltcbtc/orderbook/calculator buy spend amount' +typeFloat+ ' did not return a numbers')

        self.assertTrue((type(jsonData['sell']['avgPrice']) == int or float), '/bitfinex/ltcbtc/orderbook/calculator sell avgPrice amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['avgDelta']) == int or float), '/bitfinex/ltcbtc/orderbook/calculator sell avgDelta amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['avgDeltaBps']) == int or float), '/bitfinex/ltcbtc/orderbook/calculator sell avgDeltaBps amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['reachPrice']) == int or float), '/bitfinex/ltcbtc/orderbook/calculator sell reachPrice amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['reachDelta']) == int or float), '/bitfinex/ltcbtc/orderbook/calculator sell reachDelta amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['reachDeltaBps']) == int or float), '/bitfinex/ltcbtc/orderbook/calculator sell reachDeltaBps amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['receive']) == int or float), '/bitfinex/ltcbtc/orderbook/calculator sell spend amount' +typeFloat+ ' did not return a numbers')

        self.assertGreater(allowData['cost'], 0, '/bitfinex/ltcbtc/orderbook/calculator allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, '/bitfinex/ltcbtc/orderbook/calculator allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", '/bitfinex/ltcbtc/orderbook/calculator upgrade message was incorrect')

    # Verify the /bitfinex/ethusd/orderbook/calculator endpoint amount as an integer 
    def test_bitfinex_ethusd_orderbook_int(self):
        resp = requests.get(url + bitfinex_ethusd +'/orderbook/calculator'+ typeInt, auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertTrue((type(jsonData['buy']['avgPrice']) == int or float), '/bitfinex/ethusd/orderbook/calculator buy avgPrice amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['avgDelta']) == int or float), '/bitfinex/ethusd/orderbook/calculator buy avgDelta amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['avgDeltaBps']) == int or float), '/bitfinex/ethusd/orderbook/calculator buy avgDeltaBps amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['reachPrice']) == int or float), '/bitfinex/ethusd/orderbook/calculator buy reachPrice amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['reachDelta']) == int or float), '/bitfinex/ethusd/orderbook/calculator buy reachDelta amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['reachDeltaBps']) == int or float), '/bitfinex/ethusd/orderbook/calculator buy reachDeltaBps amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['spend']) == int or float), '/bitfinex/ethusd/orderbook/calculator buy spend amount' +typeInt+ ' did not return a numbers')

        self.assertTrue((type(jsonData['sell']['avgPrice']) == int or float), '/bitfinex/ethusd/orderbook/calculator sell avgPrice amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['avgDelta']) == int or float), '/bitfinex/ethusd/orderbook/calculator sell avgDelta amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['avgDeltaBps']) == int or float), '/bitfinex/ethusd/orderbook/calculator sell avgDeltaBps amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['reachPrice']) == int or float), '/bitfinex/ethusd/orderbook/calculator sell reachPrice amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['reachDelta']) == int or float), '/bitfinex/ethusd/orderbook/calculator sell reachDelta amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['reachDeltaBps']) == int or float), '/bitfinex/ethusd/orderbook/calculator sell reachDeltaBps amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['receive']) == int or float), '/bitfinex/ethusd/orderbook/calculator sell spend amount' +typeInt+ ' did not return a numbers')

        self.assertGreater(allowData['cost'], 0, '/bitfinex/ethusd/orderbook/calculator allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, '/bitfinex/ethusd/orderbook/calculator allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", '/bitfinex/ethusd/orderbook/calculator upgrade message was incorrect')

    # Verify the /bitfinex/ethusd/orderbook/calculator endpoint amount as a float
    def test_bitfinex_ethusd_orderbook_float(self):
        resp = requests.get(url + bitfinex_ethusd +'/orderbook/calculator'+ typeFloat, auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertTrue((type(jsonData['buy']['avgPrice']) == int or float), '/bitfinex/ethusd/orderbook/calculator buy avgPrice amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['avgDelta']) == int or float), '/bitfinex/ethusd/orderbook/calculator buy avgDelta amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['avgDeltaBps']) == int or float), '/bitfinex/ethusd/orderbook/calculator buy avgDeltaBps amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['reachPrice']) == int or float), '/bitfinex/ethusd/orderbook/calculator buy reachPrice amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['reachDelta']) == int or float), '/bitfinex/ethusd/orderbook/calculator buy reachDelta amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['reachDeltaBps']) == int or float), '/bitfinex/ethusd/orderbook/calculator buy reachDeltaBps amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['spend']) == int or float), '/bitfinex/ethusd/orderbook/calculator buy spend amount' +typeFloat+ ' did not return a numbers')

        self.assertTrue((type(jsonData['sell']['avgPrice']) == int or float), '/bitfinex/ethusd/orderbook/calculator sell avgPrice amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['avgDelta']) == int or float), '/bitfinex/ethusd/orderbook/calculator sell avgDelta amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['avgDeltaBps']) == int or float), '/bitfinex/ethusd/orderbook/calculator sell avgDeltaBps amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['reachPrice']) == int or float), '/bitfinex/ethusd/orderbook/calculator sell reachPrice amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['reachDelta']) == int or float), '/bitfinex/ethusd/orderbook/calculator sell reachDelta amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['reachDeltaBps']) == int or float), '/bitfinex/ethusd/orderbook/calculator sell reachDeltaBps amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['receive']) == int or float), '/bitfinex/ethusd/orderbook/calculator sell spend amount' +typeFloat+ ' did not return a numbers')

        self.assertGreater(allowData['cost'], 0, '/bitfinex/ethusd/orderbook/calculator allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, '/bitfinex/ethusd/orderbook/calculator allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", '/bitfinex/ethusd/orderbook/calculator upgrade message was incorrect')

    # Verify the /bitfinex/ethbtc/orderbook/calculator endpoint amount as an integer 
    def test_bitfinex_ethbtc_orderbook_int(self):
        resp = requests.get(url + bitfinex_ethbtc +'/orderbook/calculator'+ typeInt, auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertTrue((type(jsonData['buy']['avgPrice']) == int or float), '/bitfinex/ethbtc/orderbook/calculator buy avgPrice amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['avgDelta']) == int or float), '/bitfinex/ethbtc/orderbook/calculator buy avgDelta amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['avgDeltaBps']) == int or float), '/bitfinex/ethbtc/orderbook/calculator buy avgDeltaBps amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['reachPrice']) == int or float), '/bitfinex/ethbtc/orderbook/calculator buy reachPrice amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['reachDelta']) == int or float), '/bitfinex/ethbtc/orderbook/calculator buy reachDelta amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['reachDeltaBps']) == int or float), '/bitfinex/ethbtc/orderbook/calculator buy reachDeltaBps amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['spend']) == int or float), '/bitfinex/ethbtc/orderbook/calculator buy spend amount' +typeInt+ ' did not return a numbers')

        self.assertTrue((type(jsonData['sell']['avgPrice']) == int or float), '/bitfinex/ethbtc/orderbook/calculator sell avgPrice amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['avgDelta']) == int or float), '/bitfinex/ethbtc/orderbook/calculator sell avgDelta amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['avgDeltaBps']) == int or float), '/bitfinex/ethbtc/orderbook/calculator sell avgDeltaBps amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['reachPrice']) == int or float), '/bitfinex/ethbtc/orderbook/calculator sell reachPrice amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['reachDelta']) == int or float), '/bitfinex/ethbtc/orderbook/calculator sell reachDelta amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['reachDeltaBps']) == int or float), '/bitfinex/ethbtc/orderbook/calculator sell reachDeltaBps amount' +typeInt+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['receive']) == int or float), '/bitfinex/ethbtc/orderbook/calculator sell spend amount' +typeInt+ ' did not return a numbers')

        self.assertGreater(allowData['cost'], 0, '/bitfinex/ethbtc/orderbook/calculator allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, '/bitfinex/ethbtc/orderbook/calculator allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", '/bitfinex/ethbtc/orderbook/calculator upgrade message was incorrect')

    # Verify the /bitfinex/ethbtc/orderbook/calculator endpoint amount as a float
    def test_bitfinex_ethbtc_orderbook_float(self):
        resp = requests.get(url + bitfinex_ethbtc +'/orderbook/calculator'+ typeFloat, auth=(email, apiKey), params= options)
        jsonData = resp.json()['result']
        allowData = resp.json()['allowance']
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears')
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content type appears')

        self.assertTrue((type(jsonData['buy']['avgPrice']) == int or float), '/bitfinex/ethbtc/orderbook/calculator buy avgPrice amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['avgDelta']) == int or float), '/bitfinex/ethbtc/orderbook/calculator buy avgDelta amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['avgDeltaBps']) == int or float), '/bitfinex/ethbtc/orderbook/calculator buy avgDeltaBps amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['reachPrice']) == int or float), '/bitfinex/ethbtc/orderbook/calculator buy reachPrice amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['reachDelta']) == int or float), '/bitfinex/ethbtc/orderbook/calculator buy reachDelta amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['reachDeltaBps']) == int or float), '/bitfinex/ethbtc/orderbook/calculator buy reachDeltaBps amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['buy']['spend']) == int or float), '/bitfinex/ethbtc/orderbook/calculator buy spend amount' +typeFloat+ ' did not return a numbers')

        self.assertTrue((type(jsonData['sell']['avgPrice']) == int or float), '/bitfinex/ethbtc/orderbook/calculator sell avgPrice amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['avgDelta']) == int or float), '/bitfinex/ethbtc/orderbook/calculator sell avgDelta amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['avgDeltaBps']) == int or float), '/bitfinex/ethbtc/orderbook/calculator sell avgDeltaBps amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['reachPrice']) == int or float), '/bitfinex/ethbtc/orderbook/calculator sell reachPrice amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['reachDelta']) == int or float), '/bitfinex/ethbtc/orderbook/calculator sell reachDelta amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['reachDeltaBps']) == int or float), '/bitfinex/ethbtc/orderbook/calculator sell reachDeltaBps amount' +typeFloat+ ' did not return a numbers')
        self.assertTrue((type(jsonData['sell']['receive']) == int or float), '/bitfinex/ethbtc/orderbook/calculator sell spend amount' +typeFloat+ ' did not return a numbers')

        self.assertGreater(allowData['cost'], 0, '/bitfinex/ethbtc/orderbook/calculator allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, '/bitfinex/ethbtc/orderbook/calculator allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", '/bitfinex/ethbtc/orderbook/calculator upgrade message was incorrect')
