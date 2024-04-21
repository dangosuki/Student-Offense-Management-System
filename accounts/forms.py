from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

#class OrderForm(ModelForm):
    #class Meta:
        #model = Order
        #fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#anthony----------------------------------------------------------------------------
class AnthonyOffenseForm(ModelForm):
    class Meta:
        model = AnthonyOffense
        fields ='__all__'
        exclude = []

#charles----------------------------------------------------------------------------
class CharlesOffenseForm(ModelForm):
    class Meta:
        model = CharlesOffense
        fields ='__all__'
        exclude = []

#berchman----------------------------------------------------------------------------
class BerchmanOffenseForm(ModelForm):
    class Meta:
        model = BerchmanOffense
        fields ='__all__'
        exclude = []

#bosco----------------------------------------------------------------------------
class BoscoOffenseForm(ModelForm):
    class Meta:
        model = BoscoOffense
        fields ='__all__'
        exclude = []

#joseph----------------------------------------------------------------------------
class JosephOffenseForm(ModelForm):
    class Meta:
        model = JosephOffense
        fields ='__all__'
        exclude = []

#martin----------------------------------------------------------------------------
class MartinOffenseForm(ModelForm):
    class Meta:
        model = MartinOffense
        fields ='__all__'
        exclude = []

#paul==----------------------------------------------------------------------------
class PaulOffenseForm(ModelForm):
    class Meta:
        model = PaulOffense
        fields ='__all__'
        exclude = []

#anne------------------------------------------------------------------------------
class AnneOffenseForm(ModelForm):
    class Meta:
        model = AnneOffense
        fields ='__all__'
        exclude = []

#faustina---------------------------------------------------------------------------
class FaustinaOffenseForm(ModelForm):
    class Meta:
        model = FaustinaOffense
        fields ='__all__'
        exclude = []

#mary----------------------------------------------------------------------------
class MaryOffenseForm(ModelForm):
    class Meta:
        model = MaryOffense
        fields ='__all__'
        exclude = []

#rita----------------------------------------------------------------------------
class RitaOffenseForm(ModelForm):
    class Meta:
        model = RitaOffense
        fields ='__all__'
        exclude = []
        
#rose----------------------------------------------------------------------------
class RoseOffenseForm(ModelForm):
    class Meta:
        model = RoseOffense
        fields ='__all__'
        exclude = []

#rose----------------------------------------------------------------------------
class TeresaOffenseForm(ModelForm):
    class Meta:
        model = TeresaOffense
        fields ='__all__'
        exclude = []



