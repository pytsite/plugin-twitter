"""PytSite Twitter Plugin.
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def _init():
    from pytsite import assetman, lang, permissions, settings, events
    from . import _settings_form, _content_export, _eh

    # Resources
    lang.register_package(__name__, alias='twitter')
    assetman.register_package(__name__, alias='twitter')

    # Lang globals
    lang.register_global('twitter_admin_settings_url', lambda: settings.form_url('twitter'))

    # Permissions
    permissions.define_permission('twitter.settings.manage', 'twitter@manage_twitter_settings', 'app')

    # Settings
    settings.define('twitter', _settings_form.Form, 'twitter@twitter', 'fa fa-twitter', 'twitter.settings.manage')

    # Content export driver
    try:
        from plugins import content_export
        content_export.register_driver(_content_export.Driver())
    except ImportError as e:
        raise RuntimeError("Required plugin is not found: {}".format(e))

    # Event handlers
    events.listen('pytsite.router.dispatch', _eh.router_dispatch)


_init()
