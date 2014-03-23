from friendship.models import Follow
from plan.models import Plan
import traveller

__author__ = 'danielqiu'

from django import template

register = template.Library()

@register.inclusion_tag('plan/following_plan_for_index.html')
def get_following_plan(user, ):

    followings = Follow.objects.following(user)
    plan_list = []
    for f in followings:
        plan_list += user.profile.create_plan_set.filter(is_public=True)
        plan_list += user.profile.participate_plan_set.filter(is_public=True)
        plan_list = set(plan_list)


    return {'plan_list': plan_list}

