"""
    :copyright: (c) 2015 by Vitaliy Kolesov, kvs1904+github@gmail.com.
    :license: GPLv3, see LICENSE for more details.
"""

from . import views
from . import utils
from manana.application import ApplicationModule


category = ApplicationModule(
    'category',
    __package__,
)

admin_category = ApplicationModule(
    'admin_categories',
    __package__,
    url_prefix='/admin',
    static_folder='static',
    template_folder='templates',
)

admin_category.add_url_rule('/categories/', view_func=views.categories)
admin_category.add_url_rule('/ajax_tree/', view_func=views.ajax_tree)


def register(app):
    app.register_blueprint(admin_category)
    app.before_first_request_funcs.append(utils.get_root_category)
