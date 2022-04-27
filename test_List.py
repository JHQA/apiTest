import unittest
import requests

# Credentials
email = ''
apiKey = ''

# API point and options
url = 'https://api.cryptowat.ch/markets'
options = {'limit': 5, 'timeout':4}
resp = requests.get(url, auth=(email, apiKey), params= options)
jsonData = resp.json()['result']
allowData = resp.json()['allowance']
cursorData = resp.json()['cursor']

# Verify https://api.cryptowat.ch/markets
class TestMarketList(unittest.TestCase):

    # Verify the /markets api status code is 200
    def test_status_list(self):
        self.assertEqual(resp.status_code, 200, ' The wrong status code appears /markets')
    
    # Verify the /markets headers content-type is application/json
    def test_headers_list(self):
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json', ' The wrong header content-type appears /markets')

    # Verify markets/btcusd has the correct info
    def test_btcusd_list(self):
        self.assertEqual(jsonData[0]['id'], 1, 'market btcusd has an incorrect ID')
        self.assertEqual(jsonData[0]['exchange'], 'bitfinex',  'market btcusd has an incorrect exchange')
        self.assertEqual(jsonData[0]['pair'], 'btcusd', 'market btcusd has an incorrect pair')
        self.assertEqual(jsonData[0]['active'], True, 'market btcusd is not active')
        self.assertEqual(jsonData[0]['route'], 'https://api.cryptowat.ch/markets/bitfinex/btcusd', 'market btcusd has an incorrect route')

    # Verify markets/ltcusd has the correct info
    def test_ltcusd_list(self):
        self.assertEqual(jsonData[1]['id'], 2, 'market ltcusd has an incorrect ID')
        self.assertEqual(jsonData[1]['exchange'], 'bitfinex', 'market ltcusd has an incorrect exchange')
        self.assertEqual(jsonData[1]['pair'], 'ltcusd', 'market ltcusd has an incorrect pair')
        self.assertEqual(jsonData[1]['active'], True, 'market ltcusd is not active')
        self.assertEqual(jsonData[1]['route'], 'https://api.cryptowat.ch/markets/bitfinex/ltcusd', 'market ltcusd has an incorrect route')

    # Verify markets/ltcbtc has the correct info
    def test_ltcbtc_list(self):
        self.assertEqual(jsonData[2]['id'], 3, 'market ltcbtc has an incorrect ID')
        self.assertEqual(jsonData[2]['exchange'], 'bitfinex', 'market ltcbtc has an incorrect exchange')
        self.assertEqual(jsonData[2]['pair'], 'ltcbtc', 'market ltcbtc has an incorrect pair')
        self.assertEqual(jsonData[2]['active'], True, 'market ltcbtc is not active')
        self.assertEqual(jsonData[2]['route'], 'https://api.cryptowat.ch/markets/bitfinex/ltcbtc', 'market ltcbtc has an incorrect route')

    # Verify markets/ethusd has the correct info
    def test_ethusd_list(self):
        self.assertEqual(jsonData[3]['id'], 4, 'market ethusd has an incorrect ID')
        self.assertEqual(jsonData[3]['exchange'], 'bitfinex', 'market ethusd has an incorrect exchange')
        self.assertEqual(jsonData[3]['pair'], 'ethusd', 'market ethusd has an incorrect pair')
        self.assertEqual(jsonData[3]['active'], True, 'market ethusd is not active')
        self.assertEqual(jsonData[3]['route'], 'https://api.cryptowat.ch/markets/bitfinex/ethusd', 'market ethusd has an incorrect route')

    # Verify markets/ethbtc has the correct info
    def test_ethbtc_list(self):
        self.assertEqual(jsonData[4]['id'], 5, 'market ethbtc has an incorrect ID')
        self.assertEqual(jsonData[4]['exchange'], 'bitfinex', 'market ethbtc has an incorrect exchange')
        self.assertEqual(jsonData[4]['pair'], 'ethbtc', 'market ethbtc has an incorrect pair')
        self.assertEqual(jsonData[4]['active'], True, 'market ethbtc is not active')
        self.assertEqual(jsonData[4]['route'], 'https://api.cryptowat.ch/markets/bitfinex/ethbtc', 'market ethbtc has an incorrect route')

    # Verify cursor data
    def test_cursor_list(self):
        self.assertTrue(cursorData['last'], '/markets cursor "last" should not be empty')
        self.assertTrue(cursorData['hasMore'], '/markets cursor "hasMore" was not true')

    # Verify allowance data
    def test_allowance_list(self):
        self.assertGreater(allowData['cost'], 0, '/markets allowance cost was not greater than zero')
        self.assertGreaterEqual(allowData['remaining'], 0, '/markets allowance remaining was not greater or equal to zero')
        self.assertEqual(allowData['upgrade'], "For unlimited API access, create an account at https://cryptowat.ch", '/markets allowance upgrade message was incorrect')
