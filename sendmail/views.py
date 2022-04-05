from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import City


# Create your views here.
def sendmail(request):
    subject = 'welcome'
    message = 'hello friends!!'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['shreyabhat792@gmail.com']
    send_mail(subject,message,email_from,recipient_list)
    return HttpResponse("mailsent")


def pie_chart(request):
    labels = []
    data = []
    
    queryset = City.objects.all()[:5]
    for city in queryset:
        labels.append(city.name)
        data.append(city.populations)
        
        
        return render(request, 'sendmail/pie_chart.html', {
            'labels': labels,
            'data': data,
            
            
        })
    
