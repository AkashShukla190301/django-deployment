from required import views
from django.urls import path


app_name = 'required'
urlpatterns = [
    path('requirement/', views.RequirementView.as_view(), name='require'),
    path('confirm/', views.ConfirmView.as_view(), name='confirm')
]
