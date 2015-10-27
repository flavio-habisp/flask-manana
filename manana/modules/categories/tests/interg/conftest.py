"""
    :copyright: (c) 2015 by Vitaliy Kolesov, kvs1904+github@gmail.com.
    :license: GPLv3, see LICENSE for more details.
"""
import pytest
from manana.modules.categories.utils import category_create
from manana.modules.categories.utils import category_delete


@pytest.fixture(scope='module')
def tree_categories(root_category, request):
    """ build categories as:
        root_category -+
                       - Category 1.-+
                                     +- Category 1.1.
                       - Category 2.-+
                                     +- Category 2.1.

    """
    cat1 = category_create('Category 1.', root_category)
    cat2 = category_create('Category 2.', root_category)
    cat11 = category_create('Category 1.1.', cat1)
    cat21 = category_create('Category 2.1.', cat2)

    def finalize():
        category_delete(cat1, cat2)

    request.addfinalizer(finalize)
    return cat1, cat2, cat11, cat21
