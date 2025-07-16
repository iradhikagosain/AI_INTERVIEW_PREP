
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .forms import ContactForm


# Create your views here.

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

def home(request):
    return render(request, 'home.html')  


@login_required
def upload(request):
    return render(request, 'users/upload.html')

@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            body = f"""
            You have a new contact form submission:

            Name: {name}
            Email: {email}
            Message: {message}

            """

            send_mail(
                subject=f"New Contact Form: {name}",
                message=body,
                from_email=email,   
                recipient_list=['radhikagosain4@gmail.com'],  
                fail_silently=False,
            )

            return redirect('home')  

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})