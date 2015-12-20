from django.shortcuts import render
from .forms import EmailForm

# Create your views here.

#Moves the home page view to the joins app
def home(req):
	form = EmailForm() #Creates a form where we can get the email from
	context = {"form": form} 
	template = "home.html" #Picks the right template for the page
	return render(req, template, context) #Renders everything for the page 