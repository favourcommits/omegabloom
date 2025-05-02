from django.shortcuts import render, redirect

from omegaapp.models import Contact


# Create your views here.
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method == "POST":
        contactme = Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            message=request.POST['message'],
        )
        contactme.save()
        return redirect('/contact')

    else:
        return render(request, 'contact.html')
def gallery(request):
    return render(request,'gallery.html')
def index(request):
    return render(request,'index.html')
