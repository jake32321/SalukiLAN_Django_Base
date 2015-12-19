from django.db import models

# Create your models here.
class Join(models.Model):
	email = models.EmailField() #Adds a feild for the user's email
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False) #Adds the date and time to the page

	def __unicode__(self):
		return "%s"%(self.email) #Returns the email of the user that has been registered to use the site.