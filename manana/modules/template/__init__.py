"""
    :copyright: (c) 2015 by Vitaliy Kolesov, kvs1904+github@gmail.com.
    :license: GPLv3, see LICENSE for more details.
"""
from markupsafe import Markup


def jinja2_filter_css(link):
    return Markup(
        '<link href="{link}" rel="stylesheet">'.format(link=link)
    )


def jinja2_filter_javascript(link):
    return Markup(
        '<script src="{link}" ></script>'.format(link=link)
    )


def register(app):
    app.jinja_env.filters.update(
        css=jinja2_filter_css,
        js=jinja2_filter_javascript,
    )
