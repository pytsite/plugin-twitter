"""PytSite Twitter Plugin Errors.
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class AppKeyNotSet(Exception):
    pass


class AppSecretNotSet(Exception):
    pass


class SessionError(Exception):
    pass
