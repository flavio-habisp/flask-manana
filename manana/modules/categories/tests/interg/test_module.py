"""
    :copyright: (c) 2015 by Vitaliy Kolesov, kvs1904+github@gmail.com.
    :license: GPLv3, see LICENSE for more details.

"""
from manana.modules.categories.models import Category
from manana.modules.categories.utils import category_delete, category_move
from manana.modules.categories.utils import get_hierarchy_tree_of_categories


def test_root_category(tree_categories):
    assert Category.objects.count() == 5


def test_category_delete(tree_categories, root_category):
    """check that it's impossible to remove the `root` category"""
    category_delete(root_category)
    assert Category.objects.count() == 5


def test_get_hierarchy_tree_of_categories(tree_categories):
    result = get_hierarchy_tree_of_categories()
    root = result[0]
    assert root['children'][0]['title'] == 'Category 1.'
    assert root['children'][0]['children'][0]['title'] == 'Category 1.1.'
    assert root['children'][1]['title'] == 'Category 2.'
    assert root['children'][1]['children'][0]['title'] == 'Category 2.1.'


def test_move_category(root_category, tree_categories):
    """ If move `cat2` to `cat11` we would get something like:
        root+-
              -cat1-+
                    -cat11-+
                           -cat2-+
                                 -cat22

    """
    cat1, cat2, cat11, cat21 = tree_categories

    category_move(cat2, cat11)

    cat11.reload()
    cat2.reload()
    cat21.reload()

    assert cat2.rn in cat11.children
    assert cat2.rn not in root_category.children

    assert cat1.path == [root_category.rn]
    assert cat11.path == [root_category.rn, cat1.rn]
    assert cat2.path == [root_category.rn, cat1.rn, cat11.rn]
    assert cat21.path == [root_category.rn, cat1.rn, cat11.rn, cat2.rn]

    assert cat2.rn in cat11.children
    assert cat2.rn not in root_category.children
