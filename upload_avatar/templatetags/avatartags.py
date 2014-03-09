__author__ = 'danielqiu'

from django import template

register = template.Library()

@register.simple_tag
def get_avatar(user, size):
    url = '/accounts/profile/' + user.profile.get_avatar_url(size)

    return url