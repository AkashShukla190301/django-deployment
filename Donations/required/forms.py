from django import forms
from required.models import Requirement


class RequirementForm(forms.ModelForm):

    class Meta:
        model = Requirement
        fields = '__all__'
    