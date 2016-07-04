from __future__ import print_function, absolute_import, division
import requests
import json


class Client(object):
    """API for Riot Games API"""
    def __init__(self, api_key):
        self.api_key = api_key
        self.api = requests.session()
        self.api.params = {'api_key': self.api_key}

    def find_summoner(self, region, summoner):
        res = self.api.get(
            'https://{region}.api.pvp.net/api/lol/{region}'
            '/v1.4/summoner/by-name/{name}'.format(name=summoner,
                                                   region=region)).json()
        return res.get(summoner) or res.get('status')

    def get_current_game(self, region, summoner):
        res = self.api.get(
            "https://{region}.api.pvp.net/"
            "observer-mode/rest/consumer/getSpectatorGameInfo"
            "/{shard}/{summoner_id}".format(summoner_id=summoner,
                                            region=region,
                                            shard=region.upper()+'1')).json()
        return res


if __name__ == '__main__':
    test = Client('c43971d6-5eca-4aaf-bd49-6dde4ee8dbc6')
    print(json.dumps(test.get_current_game('euw', test.find_summoner('euw', 'riottmx')['id'])))
