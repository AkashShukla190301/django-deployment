from django import forms
from donate.models import BookDetail, AddressDetail
from django.contrib.auth.models import User





class BookDetailForm(forms.ModelForm):
   

    class Meta:
        model = BookDetail
        fields = '__all__'



class AddressDetailForm(forms.ModelForm):

    class Meta:
        model = AddressDetail
        fields = '__all__'
