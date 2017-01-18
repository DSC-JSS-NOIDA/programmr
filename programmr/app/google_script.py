import requests
import urllib
import simplejson as json
import random
import string


AUTHORISE_URL = 'https://accounts.google.com/o/oauth2/auth'
ACCESS_TOKEN_URL = 'https://accounts.google.com/o/oauth2/token'
REDIRECT_URL = 'http://localhost:8000/google_login/'
PROFILE_API = 'https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email'


class GooglePlus:

	access_token = None
	session_id = None

	def __init__(self, client_id, client_secret):

		self.client_id = client_id
		self.client_secret = client_secret


	def get_session_id(self, length=50):

		chars = string.uppercase + string.digits + string.lowercase
		self.session_id = ''.join(random.choice(chars) for _ in range(length))


	def get_authorize_url(self):

		self.get_session_id()
		
		authSettings = {
			'state': self.session_id,
			'redirect_uri': REDIRECT_URL,
			'response_type': 'code',
			'scope': PROFILE_API,
			'client_id': self.client_id,
		}

		params = urllib.urlencode(authSettings)
		return AUTHORISE_URL + '?' + params


	def get_access_token(self, code, state):

		if state != self.session_id:
			raise(Exception('Danger! Your established connection is compromised!!!'))

		authSettings = {
			'client_secret': self.client_secret,
			'code': code,
			'grant_type': 'authorization_code',
			'client_id': self.client_id,
			'redirect_uri': REDIRECT_URL
		}

		response = requests.post(ACCESS_TOKEN_URL, data=authSettings)
		if response.status_code != 200:
			raise(Exception('Invalid response, response code {c}'.format(c=response.status_code)))

		self.access_token = response.json()['access_token']


	def get_user_info(self):

		USER_INFO_API = 'https://www.googleapis.com/plus/v1/people/me'
		params = urllib.urlencode({'access_token': self.access_token})
		response = requests.get(USER_INFO_API + '?' + params)
		if response.status_code != 200:
			raise(Exception('Invalid response, response code {c}'.format(c=response.status_code)))

		return response.json()
