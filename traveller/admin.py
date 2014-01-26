from django.contrib import admin



# Register your models here.
from django.contrib.auth.admin import UserAdmin
from registration.models import User
from traveller.models import Traveller


#admin.site.register(Traveller)


class TravellerInline(admin.StackedInline):
    model = Traveller
    can_delete = False
    verbose_name_plural = 'traveller'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (TravellerInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)