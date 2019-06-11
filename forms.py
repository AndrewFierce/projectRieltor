from django import forms
#from captcha.fields import CaptchaField
#from phonenumber_field.modelfields import PhoneNumberField
from .choices import *

class NameForm(forms.Form):
	types = forms.ChoiceField(label='Тип помещения', choices = typePremises, initial='', widget=forms.Select(attrs={'class' : 'form-control form-control materail-input'}), required=True)
	address = forms.CharField(label='Адрес', max_length=1000, widget=forms.TextInput(attrs={'placeholder': 'Введите адрес', 'class' : 'form-control materail-input'}), required=True)
	description = forms.CharField(label='Описание', min_length=20, max_length=300, widget=forms.Textarea(attrs={'placeholder': 'Введите описание', 'class' : 'form-control materail-input'}), required=True)
	photo = forms.ImageField(label='Фото', required=True, widget=forms.FileInput(attrs={'multiple': 'multiple'}))
