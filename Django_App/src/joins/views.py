from django.shortcuts import render
from .forms import EmailForm
from .models import Join

# Create your views here.

#Moves the home page view to the joins app
def home(req):
	#print req.POST['name'], req.POST['email']
	form = EmailForm(req.POST or None) #Allows the page to be rendered if there is nothing to be posted
	if form.is_valid():
		email = form.cleaned_data['email']
		name = form.cleaned_data['name']
		new_join, created = Join.objects.get_or_create(email = email, name = name)
		print new_join, created
		print new_join.timestamp
		if created:
			print "This object was created"
	context = {"form": form} 
	template = "home.html" #Picks the right template for the page
	return render(req, template, context) #Renders everything for the page 