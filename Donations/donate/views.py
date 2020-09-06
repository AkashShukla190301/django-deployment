from django.shortcuts import render
from donate import forms
from django.views.generic import TemplateView, CreateView
from django.urls import reverse, reverse_lazy
from donate.models import BookDetail, AddressDetail
from donate.forms import BookDetailForm, AddressDetailForm

# Create your views here.


class BookDetailView(CreateView):
    model = BookDetail
    form_class = BookDetailForm
    template_name ='basicapp/book_form.html'




class AddressDetailView(CreateView):
    model = AddressDetail
    form_class = AddressDetailForm
    template_name = 'basicapp/book_address_form.html'
    success_url = reverse_lazy('donate:thankyou')



class ThankYouView(TemplateView):
    template_name = 'thankyou.html'

class welcomeView(TemplateView):
    template_name = 'welcome.html'

class aboutUsView(TemplateView):
    template_name = 'aboutus.html'