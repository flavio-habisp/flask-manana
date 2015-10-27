"""
    :copyright: (c) 2015 by Vitaliy Kolesov, kvs1904+github@gmail.com.
    :license: GPLv3, see LICENSE for more details.
"""

from flask import templating


def render_template(*args, **kwargs):
    return templating.render_template(*args, **kwargs)
