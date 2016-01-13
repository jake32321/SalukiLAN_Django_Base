from django import forms

class EmailForm(forms.Form):
	name = forms.CharField(
		required=True,
		label='Name: '
	)
	email = forms.EmailField(
		required=True,
		label='E-Mail: '
	)
	address = forms.CharField(
		required=True,
		label='Address: '
	)
	city = forms.CharField(
		required=True,
		max_length=2,
		min_length=2,
		label='City/Town: '
	)
	zipcode = forms.CharField(
		required=True,
		max_length=5,
		min_length=5,
		label='Zip Code: '
	)
	cell_number = forms.RegexField(
		required=True
		#pattern=
	)
