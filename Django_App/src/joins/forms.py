from django import forms 

class EmailForm(forms.Form):
	email = email.EmailField() 