# menu/templatetags/menu_tags.py
from django import template
from django.urls import reverse
from django.utils.safestring import mark_safe
from ..models import Menu, MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    try:
        menu = Menu.objects.prefetch_related('items').get(name=menu_name)
    except Menu.DoesNotExist:
        return ''

    active_item = None
    for item in menu.items.all():
        if item.get_url() == request.path:
            active_item = item
            break

    def build_tree(menu_items, parent=None):
        tree = []
        for item in menu_items:
            if item.parent == parent:
                children = build_tree(menu_items, item)
                tree.append({'item': item, 'children': children})
        return tree

    tree = build_tree(menu.items.all())
    return mark_safe(render_menu(tree, active_item))

def render_menu(tree, active_item):
    def is_active(item):
        return active_item and (item['item'] == active_item or is_active_in_children(item['children'], active_item))

    def is_active_in_children(children, active_item):
        for child in children:
            if child['item'] == active_item or is_active_in_children(child['children'], active_item):
                return True
        return False

    def render_item(item, is_root=False):
        active_class = 'active' if is_active(item) else ''
        children_html = ''.join(render_item(child) for child in item['children'])
        children_style = 'display: block;' if is_active(item) or is_root else 'display: none;'

        return f"""
            <li class="{active_class}">
                <a href="{item['item'].get_url()}" onclick="toggleMenu(event)">{item['item'].name}</a>
                <ul style="{children_style}">
                    {children_html}
                </ul>
            </li>
        """

    return f"<ul>{''.join(render_item(item, is_root=True) for item in tree)}</ul>"

register.simple_tag(takes_context=True)(draw_menu)
