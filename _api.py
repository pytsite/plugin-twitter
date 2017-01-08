"""PytSite Twitter Plugin API Functions.
"""
from pytsite import reg as _reg, settings as _settings
from . import _error

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def get_app_key() -> str:
    """Get application's key.
    """
    app_key = _settings.get('twitter.app_key') or _reg.get('twitter.app_key')

    if not app_key:
        raise _error.AppKeyNotSet("Configuration parameter 'twitter.app_key' is not set")

    return app_key


def get_app_secret() -> str:
    """Get application's secret key.
    """
    app_secret = _settings.get('twitter.app_secret') or _reg.get('twitter.app_secret')

    if not app_secret:
        raise _error.AppSecretNotSet("Configuration parameter 'twitter.app_secret' is not set")

    return app_secret
