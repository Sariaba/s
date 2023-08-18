from django.shortcuts import render, redirect
from app.models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def education(request):
	return render(request, "education.html")

def skills(request):
	return render(request, "skills.html")

def contact(request):
	if request.method == "POST":
		name = request.POST.get("name")
		email = request.POST.get("email")
		phone_no = request.POST.get("phone_number")
		message = request.POST.get("message")
		contact = Contact(name=name, email=email, phone_no=phone_no, message=message)
		contact.save()
		messages.success(request, "Your message has been sent successfully.")
		return redirect("/contact")
	return render(request, "contact.html")