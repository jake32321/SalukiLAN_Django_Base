from django.shortcuts import render
from .forms import EmailForm
from .models import Join
import uuid

#Attempt to get this working at a later date?

#Gets the user's IP address (Not sure if this needs to be in the final revision)
# def get_user_ip(req):
# 	try: #Checks for the user's IP under HTTP_X_FORWARDED_FOR
# 		x_forwarded = req.META.get("HTTP_X_FORWARED_FOR")
# 		if x_forwarded:
# 			ip = x_forwarded
# 		else: #Gets the user's IP under REMOTE_ADDR
# 			ip = req.META.get("REMOTE_ADDR")
# 	except: #Worst case sets as empty string
# 		ip = ""
# 	return ip

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
		# ref_id = get_uuid()
		email = form.cleaned_data['email']
		name = form.cleaned_data['name']
		address = form.cleaned_data['address']
		zipcode = form.cleaned_data['zipcode']
		cell_number = form.cleaned_data['cell_number']
		new_join, created = Join.objects.get_or_create(
			email = email,
			name = name,
			address = address,
			zipcode = zipcode,
			cell_number = cell_number
			# ref_id = ref_id
		)
		print new_join, created
		print new_join.timestamp
		if created:
			print "This object was created"
	context = {"form": form}
	template = "home.html" #Picks the right template for the page
	return render(req, template, context) #Renders everything for the page

# The bellow functions will be used to process requests for a specific page
# and this may or may not be the last changes made to this since more might
# be added or some removed.

# def about(req):
# 	print req
# 	context = {"form": form}
# 	template = "#nameoftemplate"
# 	return render(req, template, context)
#
# def event_rules(req):
# 	print req
# 	context = {"form": form}
# 	template = "#nameoftemplate"
# 	return render(req, template, context)
#
# def tournaments(req):
# 	print req
# 	context = {"form": form}
# 	template = "#nameoftemplate"
# 	return render(req, template, context)
#
# def gallery(req):
# 	print req
# 	context = {"form": form}
# 	template = "#nameoftemplate"
# 	return render(req, template, context)
#
# def sponsors(req):
# 	print req
# 	context = {"form": form}
# 	template = "#nameoftemplate"
# 	return render(req, template, context)
#
# def reserve_a_seat(req):
# 	print req
# 	context = {"form": form}
# 	template = "#nameoftemplate"
# 	return render(req, template, context)

# My Account Tab will be removed since we will send a confirmation email with
# the details regarding their reservation in 'reserve-a-seat'.  Look for updates
# in later revisions of the site.
