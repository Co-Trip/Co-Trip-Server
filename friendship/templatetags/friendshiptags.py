from django import template

from friendship.models import Follow

register = template.Library()




@register.inclusion_tag('friendship/templatetags/followers.html')
def followers(user):
    """
    Simple tag to grab all followers
    """
    # print Follow.objects.followers(user)
    return {'followers': Follow.objects.followers(user)}


@register.inclusion_tag('friendship/templatetags/following.html')
def following(user):
    """
    Simple tag to grab all users who follow the given user
    """


    return {'following': Follow.objects.following(user)}
