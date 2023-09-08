from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contactForm = ContactForm()
    
    if request.method == 'POST':
        contactForm = ContactForm(data=request.POST)
        
        if contactForm.is_valid():
            first_name = request.POST.get('first_name', '')
            last_name = request.POST.get('last_name', '')
            email = request.POST.get('email', '')
            subject = request.POST.get('subject', '')
            message = request.POST.get('message', '')
            
            email_contact = EmailMessage(
                "FútbolManía: Nuevo mensaje de contacto",
                "De {} {}<{}>\n\nAsunto:\n\n{}\n\nMensaje:\n\n{}".format(first_name, last_name, email, subject, message),
                "correo-prueba@inbox.mailtrap.io",
                ["futbolmania-contact@gmail.com"],
                reply_to=[email]
            )
            
            try:
                email_contact.send()
                return redirect(reverse('contact')+'?ok')
            except Exception as e:
                print('Error: ', type(e).__name__)
                return redirect(reverse('contact')+'?fail')
            
    return render(request, 'contact/contact.html', {'contactForm':contactForm})