"""
    :copyright: (c) 2015 by Vitaliy Kolesov, kvs1904+github@gmail.com.
    :license: GPLv3, see LICENSE for more details.
"""
import importlib
from flask import Flask
from flask.config import Config


class Application(Flask):

    def load_default_config_from_pyfile(self, filename):
        config = Config(root_path=self.root_path)
        config.from_pyfile(filename)
        for key, default_value in config.items():
            self.config.setdefault(key, default_value)


def create_application(config, app_name=None):
    app = Application(app_name or __name__)
    configure_app(app, config)
    configure_modules(app)
    return app


def configure_app(app, config):
    app.config.from_object(config)


def configure_modules(app):
    """Initialize manana's modules."""
    for module_path in app.config['MODULES']:
        module = importlib.import_module(module_path)
        assert hasattr(module, 'init_module'), \
            'Each module should contain the function `init_module`'
        module.init_module(app)
