from django.urls import path
from donate import views

app_name = 'donate'
urlpatterns = [
    path('thankyou/', views.ThankYouView.as_view(), name="thankyou"),
    path('books/', views.BookDetailView.as_view(), name='book_info'),
    path('details/', views.AddressDetailView.as_view(), name='address_detail'),
    path('about/', views.aboutUsView.as_view(), name='about')
]
