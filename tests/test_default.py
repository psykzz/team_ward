import os
from teamward.uwsgi import app as app

import unittest

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_notfound(self):
        rv = self.app.get('/gameinfo/by-player/euw/fakeplayer1234')
        print(rv.data)
        assert b'Summoner not found' in rv.data

    def test_notingame(self):
        rv = self.app.get('/gameinfo/by-player/euw/psykzz')
        print(rv.data)
        assert b'Summoner not in game' in rv.data


if __name__ == '__main__':
    unittest.main()