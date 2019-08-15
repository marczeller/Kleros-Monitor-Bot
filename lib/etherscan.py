import requests
import os
import urllib

class Etherscan:

    api_url = "https://api.etherscan.io/api?"
    api_key = os.environ["ETHERSCAN_API_KEY"]

    @classmethod
    def deposits(cls, address):

        api_options = {
            'module': 'account',
            'action': 'txlist',
            'address': address,
            'startblock': 7303699,
            'endblock': 99999999,
            'sort': 'asc',
            'apikey': cls.api_key
        }

        deposits_url = cls.api_url + urllib.parse.urlencode(api_options)
        response = requests.get(deposits_url)
        get_json = response.json()
        items = get_json['result']
        filtered_items = []
        for item in items:
            if item['value'] != '0' and item['isError'] != '1' and item['to'] != address : filtered_items.append(item)
        return filtered_items
