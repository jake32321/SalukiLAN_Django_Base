from django.shortcuts import render

# Create your views here.

#Moves the home page view to the joins app
def home(req):
	context = {} #Imports the python dictionary
	template = "home.html" #Picks the right template for the page
	return render(req, template, context) #Renders everything for the page 