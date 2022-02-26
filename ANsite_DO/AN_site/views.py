from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here
def home(request):
    return render(request, 'Home.html', {})


def about(request):
    return render(request, 'About.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            "Message from " + str(message_name),
            message,
            message_email,
            ['info@adrenalinenomads.com'],
            fail_silently=False,
            )
        return render(request, 'Contact.html', {'message_name': message_name})
    else:
        return render(request, 'Contact.html', {})
