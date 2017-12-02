"""PytSite Twitter Plugin Event Handlers
"""
from pytsite import lang as _lang, router as _router, reg as _reg
from plugins import  auth as _auth

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def router_dispatch():
    """'pytsite.router.dispatch' event handler.
    """
    if _auth.get_current_user().has_permission('twitter@manage_settings'):
        if not _reg.get('twitter.app_key') or not _reg.get('twitter.app_secret'):
            _router.session().add_warning_message(_lang.t('twitter@plugin_setup_required_warning'))
