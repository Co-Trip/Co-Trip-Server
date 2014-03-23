try:
    from django.conf.urls import url, patterns
except ImportError:
    from django.conf.urls.defaults import url, patterns
from friendship.views import followers, following, follower_add, follower_remove, all_users, is_following

urlpatterns = patterns('',
    url(
        regex=r'^users/$',
        view=all_users,
        name='friendship_view_users',
    ),

    url(
        regex=r'^followers/(?P<username>[\w-]+)/$',
        view=followers,
        name='friendship_followers',
    ),
    url(
        regex=r'^following/(?P<username>[\w-]+)/$',
        view=following,
        name='friendship_following',
    ),
    url(
        regex=r'^follower/add/(?P<followee_username>[\w-]+)/$',
        view=follower_add,
        name='follower_add',
    ),
    url(
        regex=r'^follower/remove/(?P<followee_username>[\w-]+)/$',
        view=follower_remove,
        name='follower_remove',
    ),
    url(
        regex=r'^follower/is_following/(?P<followee_username>[\w-]+)/$',
        view=is_following,
        name='is_following',
    ),
)
