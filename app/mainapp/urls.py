from django.urls import path
from mainapp.views import MainListView, ContactListView, EmailView, ConditionerListView

app_name = 'mainapp'

urlpatterns = [
    path('', MainListView.as_view(), name='index'),
    path('contact/', ContactListView.as_view(), name='contact'),
    path('conditioner/', ConditionerListView.as_view(), name='conditioner'),
    path('email/', EmailView.as_view(), name='send_email'),
]