"""
    :copyright: (c) 2015 by Vitaliy Kolesov, kvs1904+github@gmail.com.
    :license: GPLv3, see LICENSE for more details.
"""


class ConfigDev(object):
    SECRET_KEY = '<Put here you some SECRET_KEY>'
    TESTING = True
    DEBUG = True
    THEME = {
        'BACKEND': 'admin_base.html'
    }
    MODULES = (
        'manana.modules.template',
        'manana.modules.mongodb',
        'manana.modules.debugtoolbar',
        'manana.modules.categories',
    )


class ConfigTest(ConfigDev):
    MONGODB_DB = 'manana_test'
    DEBUG_TB_ENABLED = False
