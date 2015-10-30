"""
    :copyright: (c) 2015 by Vitaliy Kolesov, kvs1904+github@gmail.com.
    :license: GPLv3, see LICENSE for more details.
"""
from jinja2.environment import Template
from manana.core.template import render_template


def test_render_template(app):
    tmp = 'text out of the block and {% block inner %}{{ vars }}{% endblock %}'
    template = Template(tmp)

    case1 = render_template(
        template,
        vars='text inside the block'
    )

    case2 = render_template(
        template,
        vars='text inside the block',
        block='inner'
    )

    assert 'text out of the block and text inside the block' == case1
    assert 'text inside the block' == case2
