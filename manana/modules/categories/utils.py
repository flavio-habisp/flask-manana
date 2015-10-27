"""
    :copyright: (c) 2015 by Vitaliy Kolesov, kvs1904+github@gmail.com.
    :license: GPLv3, see LICENSE for more details.
"""
from . import models


def get_root_category():
    if not hasattr(get_root_category, 'instance'):
        get_root_category.instance = (
            models.Category.get(models.ROOT_CATEGORY_RN)
            or
            models.Category(
                rn=models.ROOT_CATEGORY_RN,
                title='Categories',
                enabled=True
            ).save()
        )
    return get_root_category.instance


def category_create(title, parent, enabled=True, **kwargs):
    _path = parent.path.copy()
    _path.append(parent.rn)

    instance = models.Category(
        title=title,
        parent=parent,
        enabled=enabled,
        path=_path,
        **kwargs
    ).save()
    parent.children.append(instance.rn)
    parent.save()
    return instance


def category_delete(*args):
    for category in args:
        parent_category = category.parent
        if parent_category:
            parent_category.children.remove(category.rn)
            parent_category.save()
            category.delete()


def get_hierarchy_tree_of_categories():
    _stack = _get_hashed_categories()
    result = []

    def add(data, category=None):
        _category = category or get_root_category()
        element = dict(
            title=_category.title,
            key=_category.rn,
            folder=_category.has_children,
            children=list(),
            expanded=_category.has_children,
        )
        data.append(element)
        if _category.has_children:
            for child_rn in _category.children:
                add(element['children'], _stack[str(child_rn)])
        return data

    return add(result)


def _get_hashed_categories():
    _stack = {}
    for category in models.Category.objects:
        _stack[str(category.rn)] = category
    return _stack
