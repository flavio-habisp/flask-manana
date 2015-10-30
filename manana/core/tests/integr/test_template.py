"""
    :copyright: (c) 2015 by Vitaliy Kolesov, kvs1904+github@gmail.com.
    :license: GPLv3, see LICENSE for more details.
"""
from jinja2.environment import Template
from manana.core.template import render_template


def test_render_template_case1(app):
    template = Template(
        'text out of the block and {% block inner %}{{ vars }}{% endblock %}'
    )
    case1 = render_template(
        template,
        vars='text inside the block'
    )
    assert 'text out of the block and text inside the block' == case1


def test_render_template_case2(app):
    template = Template(
        'text out of the block and {% block inner %}{{ vars }}{% endblock %}'
    )
    case2 = render_template(
        template,
        vars='TEST',
        block='inner'
    )

    assert 'TEST' == case2


def test_render_template_case3(app):
    case3 = render_template(
        Template(
            """
            {% block outer %}
            {% block inner -%}
                TEST
            {%- endblock %}
            {% endblock %}
            """),
        block='inner'
    )

    assert 'TEST' == case3
