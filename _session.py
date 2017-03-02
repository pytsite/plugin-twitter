"""PytSite Twitter Session.
"""
from datetime import datetime as _dt
from requests_oauthlib import OAuth1Session
from pytsite import router as _router
from . import _api, _error

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class Session:
    """Twitter oAuth Driver.
    """

    def __init__(self, oauth_token: str, oauth_token_secret: str, app_key: str = None, app_secret: str = None):
        """Init.
        """
        self._app_key = app_key or _api.get_app_key()
        self._app_secret = app_secret or _api.get_app_secret()
        self._oauth_token = oauth_token
        self._oauth_token_secret = oauth_token_secret

    def _init_session(self, callback_uri: str = None):
        callback_uri = callback_uri or _router.current_url()

        if self._get_state()['stage'] == 'new':
            # Need to fetch request token
            oauth = OAuth1Session(self._app_key, self._app_secret, callback_uri=callback_uri)
            r_token_resp = oauth.fetch_request_token('https://api.twitter.com/oauth/request_token')
            self._set_state({
                'stage': 'request_token',
                'time': _dt.now(),
                'oauth_token': r_token_resp.get('oauth_token'),
                'oauth_token_secret': r_token_resp.get('oauth_token_secret')
            })

    def _get_state(self) -> dict:
        """Get state.
        """
        if self._oauth_token and self._oauth_token_secret:
            return {'stage': 'ready'}

        default = {
            'stage': 'new',
            'time': _dt.now(),
            'oauth_token': None,
            'oauth_token_secret': None
        }
        state = _router.session().get('oauth.twitter.session')

        if not state or (_dt.now() - state['time']).seconds > 60:
            state = default

        return state

    def _set_state(self, state: dict):
        """Set state.
        """
        _router.session()['oauth.twitter.session'] = state

        return self

    def _clear_state(self):
        """Clear state.
        """
        if 'oauth.twitter.session' in _router.session():
            del _router.session()['oauth.twitter.session']

        return self

    def get_authorization_url(self, callback_uri: str = None) -> str:
        """Get authorization URL.
        """
        callback_uri = callback_uri or _router.current_url()

        self._init_session(callback_uri)

        state = self._get_state()
        if state['stage'] != 'request_token':
            raise _error.SessionError("Cannot generate authorization URL.")

        oauth = OAuth1Session(self._app_key, self._app_secret, state['oauth_token'], state['oauth_token_secret'],
                              callback_uri=callback_uri)

        return oauth.authorization_url('https://api.twitter.com/oauth/authorize')

    def get_access_token(self, verifier: str) -> dict:
        """Exchange request token to access token.
        """
        self._init_session()

        state = self._get_state()
        if state['stage'] != 'request_token':
            raise _error.SessionError('Session expired')
        self._clear_state()

        session = OAuth1Session(self._app_key, self._app_secret,
                                state['oauth_token'], state['oauth_token_secret'],
                                verifier=verifier)

        return session.fetch_access_token('https://api.twitter.com/oauth/access_token')
