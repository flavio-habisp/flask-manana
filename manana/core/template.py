"""
    :copyright: (c) 2015 by Vitaliy Kolesov, kvs1904+github@gmail.com.
    :license: GPLv3, see LICENSE for more details.
"""

from flask import templating
from flask.globals import current_app


def render_template(template, **kwargs):
    if 'block' in kwargs:
        block_key = kwargs.pop('block')
        return render_block(template, block_key, **kwargs)
    return templating.render_template(template, **kwargs)


def render_block(template, blockname, **kwargs):
    if isinstance(template, (str,)):
        current_app.update_template_context(kwargs)
        template = current_app.jinja_env.get_template(template)
    context = template.new_context(kwargs)
    return ''.join(template.blocks[blockname](context))
