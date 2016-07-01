from __future__ import print_function, absolute_import, division

import os

from flask import Flask, jsonify, g
app = Flask(__name__)

from teamward.RiotAPI import Client


@app.before_request
def before_request():
	# Create the api client
	g.api = Client(os.environ.get('API_KEY'))


@app.route('/gameinfo/by-player/<region>/<summoner>')
def index(region, summoner):

	summoner_info = g.api.find_summoner(region, summoner)
	if summoner_info.get('status_code', 0) == 404:
		return jsonify({'status': 'error', 
			'error_code': 404, 
			'reason': 'Summoner not found'})

	game = g.api.get_current_game(region, summoner_info['id'])
	if not game:
		return jsonify({
			'status': 'error', 
			'error_code': 405, 
			'reason': 'Summoner not in game'})

	return jsonify({

		})

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')