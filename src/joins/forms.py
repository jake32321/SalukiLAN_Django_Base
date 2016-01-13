from django import forms

class EmailForm(forms.Form):
	name = forms.CharField(required = True)
	email = forms.EmailField(required = True)
	address = forms.CharField(required = True)
	zipcode = forms.CharField(required = True)
	cell_number = forms.CharField(required = True)
