"""PytSite Twitter API Plugin.
"""
from ._api import get_app_key, get_app_secret
from . import _error as error, _session as session, _widget as widget

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def _init():
    from pytsite import lang, router
    from plugins import settings, permissions
    from . import _settings_form, _eh

    # Resources
    lang.register_package(__name__)

    # Lang globals
    lang.register_global('twitter_admin_settings_url', lambda language, args: settings.form_url('twitter'))

    # Permissions
    permissions.define_permission('twitter@manage_settings', 'twitter@manage_twitter_settings', 'app')

    # Settings
    settings.define('twitter', _settings_form.Form, 'twitter@twitter', 'fa fa-twitter', 'twitter@manage_settings')

    # Event handlers
    router.on_dispatch(_eh.router_dispatch)


_init()
