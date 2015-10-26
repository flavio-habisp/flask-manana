"""
    :copyright: (c) 2015 by Vitaliy Kolesov, kvs1904+github@gmail.com.
    :license: GPLv3, see LICENSE for more details.
"""

from flask_mongoengine import MongoEngine

db = MongoEngine()


def init_module(app):
    app.load_default_config_from_pyfile('modules/db/config.py')
    db.init_app(app)
