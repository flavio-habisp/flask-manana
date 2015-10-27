"""
    :copyright: (c) 2015 by Vitaliy Kolesov, kvs1904+github@gmail.com.
    :license: GPLv3, see LICENSE for more details.
"""


from flask_debugtoolbar import DebugToolbarExtension


def register(app):
    app.load_default_config_from_pyfile(
        'modules/debugtoolbar/config.py'
    )
    DebugToolbarExtension(app)
