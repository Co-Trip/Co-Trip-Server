from django.contrib import admin

from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from django.forms.extras import SelectDateWidget
from city.models import City
from django.db.models.signals import post_save
from django.forms import ModelForm
from django.db import models
from django import forms
# Create your models here.
from upload_avatar.models import UploadAvatarMixIn
from upload_avatar.signals import avatar_crop_done

GENDER_CHOICES= (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),

    )

class Traveller(models.Model, UploadAvatarMixIn):
    user = models.OneToOneField(User, related_name='profile')
    gender = models.CharField(max_length=15, null=True, choices=GENDER_CHOICES)

    birthday = models.DateField(null=True)
    city = models.ForeignKey(City, blank=True, null=True)
    avatar_name = models.CharField(max_length=128, null=True)

    def __unicode__(self):
        return u'%s' % self.user.username


    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={'profile_id': self.id})

    def get_avatar_name(self, size):
        return UploadAvatarMixIn.build_avatar_name(self, self.avatar_name, size)

def save_avatar_in_db(sender, uid, avatar_name, **kwargs):
    if Traveller.objects.filter(user_id=uid).exists():
        Traveller.objects.filter(user_id=uid).update(avatar_name=avatar_name)
    else:
        Traveller.objects.create(user_id=uid, avatar_name=avatar_name)

avatar_crop_done.connect(save_avatar_in_db)


class TravellerAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return True

admin.site.register(Traveller, TravellerAdmin)

class ProfileEditForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        try:
            self.fields['email'].initial = self.instance.user.email
            self.fields['username'].initial = self.instance.user.username

        except User.DoesNotExist:
            pass

    city = forms.ModelChoiceField(queryset=City.objects.all())
    username = forms.CharField(max_length=30, required=True, label='username')
    email = forms.EmailField(label="Email")

    class Meta:
        model = Traveller
        fields = ['username', 'email', 'city', 'birthday', 'gender']
        widgets = {
            'birthday': SelectDateWidget(required=False),

        }

    def save(self, *args, **kwargs):
        u = self.instance.user
        u.email = self.cleaned_data['email']
        u.save()
        new_profile = super(ProfileEditForm, self).save(*args, **kwargs)
        return new_profile


User.profile = property(lambda u: Traveller.objects.get_or_create(user=u)[0])


def profile(sender, **kwargs):
    if kwargs.get('created', False):
        Traveller.objects.create(
            user=kwargs.get('instance')
        )


post_save.connect(profile, sender=User)




