"""
    :copyright: (c) 2015 by Vitaliy Kolesov, kvs1904+github@gmail.com.
    :license: GPLv3, see LICENSE for more details.
"""
import pytest
from flask_mongoengine import MongoEngine

from manana.application import create_application
from manana import config
from manana.modules.categories.utils import get_root_category


@pytest.fixture(scope='session')
def app():
    return create_application(config.ConfigTest)


@pytest.fixture(scope='session')
def db(app):
    db = app.extensions['mongoengine']
    db_name = app.config['MONGODB_DB']
    client = db.connection
    client.drop_database(db_name)
    return MongoEngine(app)


@pytest.fixture(scope='session')
def root_category(db):
    return get_root_category()
