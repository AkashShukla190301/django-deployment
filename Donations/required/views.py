from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from required.models import Requirement
from required.forms import RequirementForm
from django.urls import reverse_lazy
# Create your views here.

class RequirementView(CreateView):
    model= Requirement
    form_class = RequirementForm
    template_name= 'required/requirement.html'
    success_url = reverse_lazy('required:confirm')


class ConfirmView(TemplateView):
    template_name = "required/Confirmation.html"