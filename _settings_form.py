"""PytSite Twitter Plugin Settings Form.
"""
from pytsite import widget as _widget, lang as _lang, settings as _settings

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class Form(_settings.Form):
    def _setup_widgets(self):
        self.add_widget(_widget.input.Text(
            uid='setting_app_key',
            weight=10,
            label=_lang.t('twitter@app_key'),
            required=True,
            help=_lang.t('twitter@app_key_setup_help'),
        ))

        self.add_widget(_widget.input.Text(
            uid='setting_app_secret',
            weight=20,
            label=_lang.t('twitter@app_secret'),
            required=True,
            help=_lang.t('twitter@app_secret_setup_help'),
        ))

        super()._setup_widgets()
