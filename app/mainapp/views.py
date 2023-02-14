from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic import ListView, View
from django.conf import settings
from django.core.mail import send_mail


class MainListView(ListView):
    model = User
    template_name = 'mainapp/index.html'


class EmailView(View):
    def get(self, request):
        return redirect("mainapp:index")

    def post(self, request):
        try:
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']

            title = f'САЙТ - новое письмо. Тема {subject}'
            email_body = f'Имя: {name}\nEmail: {email}\nСообщение: {message}'
            send_mail(title, email_body, settings.EMAIL_HOST_USER, ['sharov-a83@mail.ru'])
        except Exception as e:
            print('ERROR:', e)
        return redirect("mainapp:index")