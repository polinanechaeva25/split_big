from django.urls import path
from mainapp.views import MainListView, ContactListView, EmailView

app_name = 'mainapp'

urlpatterns = [
    path('', MainListView.as_view(), name='index'),
    path('contact/', ContactListView.as_view(), name='contact'),
    path('email/', EmailView.as_view(), name='send_email'),
]