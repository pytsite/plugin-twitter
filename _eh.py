"""PytSite Twitter Plugin Event Handlers
"""
from pytsite import lang as _lang, router as _router
from plugins import settings as _settings, auth as _auth

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def router_dispatch():
    """'pytsite.router.dispatch' event handler.
    """
    if _auth.get_current_user().has_permission('twitter.settings.manage'):
        if not _settings.get('twitter.app_key') or not _settings.get('twitter.app_secret'):
            _router.session().add_warning_message(_lang.t('twitter@plugin_setup_required_warning'))
