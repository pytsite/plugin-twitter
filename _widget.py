"""PytSite Twitter Plugin Auth Widget.
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import html as _html, lang as _lang, router as _router
from plugins import widget as _widget
from ._session import Session as TwitterSession


class Auth(_widget.Abstract):
    def __init__(self, uid: str, **kwargs):
        """Init.
        """
        super().__init__(uid, **kwargs)

        self._oauth_token = kwargs.get('oauth_token', '')
        self._oauth_token_secret = kwargs.get('oauth_token_secret', '')
        self._user_id = kwargs.get('user_id', '')
        self._screen_name = kwargs.get('screen_name', '')
        self._callback_uri = kwargs.get('callback_uri', '')

        self._css += ' widget-twitter-oauth'

        self._session = TwitterSession(self.oauth_token, self.oauth_token_secret)
        """:type: plugins.twitter._oauth.Driver"""

    @property
    def oauth_token(self) -> str:
        return self._oauth_token

    @property
    def oauth_token_secret(self) -> str:
        return self._oauth_token_secret

    @property
    def user_id(self) -> str:
        return self._user_id

    @property
    def screen_name(self) -> str:
        return self._screen_name

    def _get_element(self, **kwargs) -> _html.Element:
        """Render widget.
        :param **kwargs:
        """
        # If 'verifier' is here, we need to exchange it to an access token
        if not self._user_id:
            inp_oauth_verifier = _router.request().inp.get('oauth_verifier')
            if inp_oauth_verifier:
                token = self._session.get_access_token(inp_oauth_verifier)
                self._oauth_token = token['oauth_token']
                self._oauth_token_secret = token['oauth_token_secret']
                self._user_id = token['user_id']
                self._screen_name = token['screen_name']

        wrapper = _html.TagLessElement()

        wrapper.append(_widget.input.Hidden(
            uid=self.uid + '[oauth_token]',
            value=self.oauth_token,
        ).renderable())

        wrapper.append(_widget.input.Hidden(
            uid=self.uid + '[oauth_token_secret]',
            value=self.oauth_token_secret,
        ).renderable())

        wrapper.append(_widget.input.Hidden(
            uid=self.uid + '[user_id]',
            value=self.user_id,
        ).renderable())

        wrapper.append(_widget.input.Hidden(
            uid=self.uid + '[screen_name]',
            value=self.screen_name,
        ).renderable())

        if self.screen_name:
            title = self.screen_name
            href = 'https://twitter.com/' + self._screen_name
        else:
            title = _lang.t('twitter@authorization')
            href = self._session.get_authorization_url(self._callback_uri)

        a = _html.A(title, href=href)
        a.append(_html.I(css='fa fa-twitter'))
        wrapper.append(_widget.static.HTML(
            uid=self.uid + '[auth_link]',
            em=a,
        ).renderable())

        return wrapper
