"""
    :copyright: (c) 2015 by Vitaliy Kolesov, kvs1904+github@gmail.com.
    :license: GPLv3, see LICENSE for more details.
"""
from flask.templating import render_template_string


def test_filter_css(app):
    result = render_template_string('{{"http://example.com"|css}}')
    assert result == '<link href="http://example.com" rel="stylesheet">'


def test_filter_js(app):
    result = render_template_string('{{"http://example.com/"|js}}')
    assert result == '<script src="http://example.com/" ></script>'
