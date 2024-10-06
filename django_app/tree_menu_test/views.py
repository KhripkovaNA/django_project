from django.shortcuts import render
from django.http import Http404
from django.urls import resolve
from tree_menu.models import MenuItem, Menu


# Homepage
def index(request):
    return render(request, 'index.html', {
        'title': 'Home',
        'menus': Menu.objects.all()
    })


def menu_pages(request):
    # Resolve the named URL from the current path
    url = request.path_info
    named_url = resolve(url).url_name

    # Get the menu item by URL or named URL
    menu_item = MenuItem.objects.filter(url=url).first() or MenuItem.objects.filter(named_url=named_url).first()

    if menu_item:
        # Render the corresponding template or menu item content
        return render(request, 'pages.html', {
            'title': menu_item.name,
            'menu': menu_item.menu.name,
            'page_name': menu_item.name,
        })
    else:
        # Handle the case where the menu item is not found (404)
        raise Http404("Page is not found")
