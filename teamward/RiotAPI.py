import requests


class Client(object):
	"""API for Riot Games API"""
	def __init__(self, api_key):
		self.api_key = api_key
		self.api = requests.session()

	def find_summoner(self, region, summoner):
		params = {'api_key': self.api_key}
		res = self.api.get('https://{region}.api.pvp.net/api/lol/{region}'
			'/v1.4/summoner/by-name/{name}'.format(
				name=summoner, region=region), params=params).json()
		return res.get(summoner) or res.get('status')

	def is_ingame(self, region, summoner):
		return False
