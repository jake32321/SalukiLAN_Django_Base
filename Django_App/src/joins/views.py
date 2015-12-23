from django.shortcuts import render
from .forms import EmailForm
from .models import Join
import uuid

#Attempt to get this working at a later date?

#Gets the user's IP address
def get_user_ip(req):
	try: #Checks for the user's IP under HTTP_X_FORWARDED_FOR
		x_forwarded = req.META.get("HTTP_X_FORWARED_FOR")
		if x_forwarded:
			ip = x_forwarded
		else: #Gets the user's IP under REMOTE_ADDR
			ip = req.META.get("REMOTE_ADDR")
	except: #Worst case sets as empty string
		ip = ""
	return ip

#Creates a unique identifier for each user
def get_uuid():
	ref_id = str(uuid.uuid4())[:10].replace('-', '').upper() #Strictly formatting
	try: #Makes sure the identifier doesn't already exist
		id_exists = Join.objects.get(ref_id=ref_id)
		get_uuid()
	except:
		return ref_id

#Moves the home page view to the joins app
def home(req):
	#print req.POST['name'], req.POST['email']
	form = EmailForm(req.POST or None) #Allows the page to be rendered if there is nothing to be posted
	if form.is_valid():
		ref_id = get_uuid()
		email = form.cleaned_data['email']
		name = form.cleaned_data['name']
		ip_address = get_user_ip(req)
		new_join, created = Join.objects.get_or_create(email = email, name = name, ip_address = ip_address, ref_id = ref_id)
		print new_join, created
		print new_join.timestamp
		if created:
			print "This object was created"
	context = {"form": form} 
	template = "home.html" #Picks the right template for the page
	return render(req, template, context) #Renders everything for the page 