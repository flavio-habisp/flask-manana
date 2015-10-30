"""
    :copyright: (c) 2015 by Vitaliy Kolesov, kvs1904+github@gmail.com.
    :license: GPLv3, see LICENSE for more details.
"""
import json

from manana.core.template import render_template
from manana.modules.categories.utils import get_hierarchy_tree_of_categories


def categories():
    return render_template('admin_categories/index.html')


def category_tree_ajax():
    return json.dumps(get_hierarchy_tree_of_categories())
