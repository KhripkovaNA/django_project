from django import template
from django.urls import resolve
from ..models import MenuItem
from django.db import models


# register the custom template tag with Django’s template system
register = template.Library()


def get_parents(menu_item):
    """Recursive function for getting parent menu items"""
    parents = []
    while menu_item.parent:
        parents.append(menu_item.parent)
        menu_item = menu_item.parent
    return parents[::-1]  # reverse list to have access to the root parent


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_url = request.path_info
    current_url_name = resolve(request.path_info).url_name

    # load menu items preloading all associate menu elements
    menu_items = MenuItem.objects.filter(menu__name=menu_name).select_related('parent').prefetch_related('children')

    # find active menu item based on current URL
    active_item = menu_items.filter(models.Q(url=current_url) | models.Q(named_url=current_url_name)).first()

    # get active item's parent items
    active_parents = get_parents(active_item) if active_item else []

    # get top-level menu items
    top_items = menu_items.filter(parent__isnull=True)

    return {
        'menu_items': top_items,
        'current_url': current_url,
        'active_parents': active_parents
    }
