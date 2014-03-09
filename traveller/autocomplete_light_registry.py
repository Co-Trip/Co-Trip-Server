from django.contrib.auth.models import User

__author__ = 'danielqiu'
import autocomplete_light
from models import Traveller

class UserAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['username']
    model = User


autocomplete_light.register(User, UserAutocomplete)