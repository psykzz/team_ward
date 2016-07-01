from __future__ import print_statement, absolute_imports, division
import os

from flask import Flask
import requests

app = Flask(__name__)

api_key = os.environ.get('API_KEY')


