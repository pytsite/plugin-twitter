"""PytSite Twitter Plugin.
"""
from pytsite import assetman as _assetman, lang as _lang, permissions as _permissions, settings as _settings, \
    events as _events
from . import _settings_form, _content_export, _eh

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

# Resources
_lang.register_package(__name__, alias='twitter')
_assetman.register_package(__name__, alias='twitter')

# Lang globals
_lang.register_global('twitter_admin_settings_url', lambda language, args: _settings.form_url('twitter'))

# Permissions
_permissions.define_permission('twitter.settings.manage', 'twitter@manage_twitter_settings', 'app')

# Settings
_settings.define('twitter', _settings_form.Form, 'twitter@twitter', 'fa fa-twitter', 'twitter.settings.manage')

# Content export driver
try:
    from plugins import content_export

    content_export.register_driver(_content_export.Driver())
except ImportError as e:
    raise RuntimeError("Required plugin is not found: {}".format(e))

# Event handlers
_events.listen('pytsite.router.dispatch', _eh.router_dispatch)
