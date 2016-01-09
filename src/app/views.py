
####################################################################

#APP IS MEANT TO BE A DEMONSTRATION 

#Author: Jacob Reed
#Last Update: 5 December 2015
#GitHub Repo: https://github.com/jake32321/Django_Interview_Prep.git

####################################################################

from django.shortcuts import render

#Defining the home view that will be requested at the start of the page 
# def home(req):
# 	context = {} #Imports the python dictionary
# 	template = "home.html" #Picks the right template for the page
# 	return render(req, template, context) #Renders everything for the page 

# ALl you would need to do for another page is make a copy of the function for the request and rename it 
# def home2(req):
# 	context = {} 
# 	template = "home2.html" 
# 	return render(req, template, context)  