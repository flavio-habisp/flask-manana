"""
    :copyright: (c) 2015 by Vitaliy Kolesov, kvs1904+github@gmail.com.
    :license: GPLv3, see LICENSE for more details.
"""


class ConfigDev(object):
    TESTING = True
    DEBUG = True

    ACTIVATE_MODULES = (
        'manana.modules.db',
    )
