from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from django.forms.extras import SelectDateWidget
from cities_light.models import City
# Create your models here.
from django.db.models.signals import post_save
from django.forms import ModelForm
from django.db import models
from django import forms


class Traveller(models.Model):
    user = models.OneToOneField(User)
    birthday = models.DateField(null=True)
    city = models.ForeignKey(City, blank=True, null=True)
    friends = models.ManyToManyField('traveller.Traveller')

    def __unicode__(self):
        return u'%s' % (self.user.username)


class ProfileEditForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        try:
            self.fields['email'].initial = self.instance.user.email
            self.fields['username'].initial = self.instance.user.username

        except User.DoesNotExist:
            pass

    city = forms.ModelChoiceField(queryset=City.objects.filter(country='48').all())
    username = forms.CharField(max_length=30, required=True, label=('username'))
    email = forms.EmailField(label=("Email"))



    class Meta:
        model = Traveller
        fields = ['username', 'email', 'city', 'birthday', 'friends']
        widgets = {
        'birthday': SelectDateWidget(required=False),

        }

    def save(self, *args, **kwargs):
        u = self.instance.user
        u.email = self.cleaned_data['email']
        u.save()
        profile = super(ProfileEditForm, self).save(*args, **kwargs)
        return profile





User.profile = property(lambda u: Traveller.objects.get_or_create(user=u)[0])


def profile(sender, **kwargs):
    if kwargs.get('created', False):
        Traveller.objects.create(
            user=kwargs.get('instance')
        )


post_save.connect(profile, sender=User)