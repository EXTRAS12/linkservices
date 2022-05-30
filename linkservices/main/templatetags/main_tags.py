from django import template
from link_app.models import Link
from site_app.models import WebSite

from users.models import User

from main.models import Plugin

register = template.Library()


@register.simple_tag()
def show_count_link():
    item = Link.objects.all().count()

    return item


@register.simple_tag()
def show_count_site():
    site = WebSite.objects.all().count()

    return site


@register.simple_tag()
def show_count_user():
    user = User.objects.all().count()

    return user


@register.inclusion_tag('main/partials/plugins_tpl.html')
def show_plugins():
    plugins = Plugin.objects.all()[:3]
    return {"plugins": plugins}
