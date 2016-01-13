from django.db import models

# Create your models here.
class Join(models.Model):
	email = models.EmailField() #Adds a feild for the user's email
	# ip_address = models.CharField(max_length=120, default='127.0.0.1') #Sets the variable to the user's current IP
	# ref_id = models.CharField(max_length=120, default='Default VALUE')
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False) #Adds the date and time to the page
	updates = models.DateTimeField(auto_now_add = False, auto_now = True)
	name = models.TextField()
	address = models.TextField()
	city = models.TextField()
	state = model.CharField(max_length=2, default='xx')
	zipcode = models.CharField(max_length=120, default='xxxx')
	cell_number = models.CharField(max_length=120, default='(xxx) xxx-xxxx')

	def __unicode__(self):
		return "%s"%(self.email) #Returns the email of the user that has been registered to use the site.

#Makes the email unique to the refference identifier
class Meta:
	unique_together = ("email", "ref_id",)
