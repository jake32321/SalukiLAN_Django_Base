## SalukiLAN Django Base

![SalukiLAN logo](./SLAN.png)

## A Word from the noble Jake 

Hello!  Below is something I posted on #sigweb (I believe) a couple days ago.  This is just an update and no final decisions have been made yet.  Please read this and get back to me ASAP!  I need people who are really interested to tell me that they want in.  If you want in let me know where you feel strongest working (front or back end) let me know.  If you don't know where you'd fit best message me and we will figure something out.  We need to really get cranking on this really really quick.  Join #sigweb for more updates and let me know if you have absolutely any questions and better sooner than later! Thank You!

"I've been messing around with Django.  For our purposes it might be the better option.  We can always use node and express but we'll have to do a crap ton of formatting.  If we use Django we shouldn't have to do that.  I'm open to see what everyone else thinks.   Once we make a final decision on which one to use the people wo want to help will need to really work on learning the framework.  I've found various YouTube videos that show you how to configure, run, develop, and deploy the apps.  If we do the Node route there will be considerably large amounts of JS.  If we do the Django route there is a lot of Python.  If we do the Django route we should be able to leave a majority of the site the way it is right now but adding it to a views folder where we can let Django do the rendering for us and we don't have to mess with special formatting (unless we want to).  If I remember right the general consensus is that there are more people who are familiar with python and less with JS.  Might be easier to go the Django route in my mind. If we decide to make a Django based app I will want two different "teams".  One to handle front end stuff and the other to do backend.  I will probably do a lot of the backend programming along with anyone who is strong in python.  I don't know if we've progressed past where we could do this in an agile manner but I need to talk to people to see what is left to be done.  What I really really need is motivation from people who want to help though.  I know the project has been a stick in the mud recently and I haven't helped that but I absolutely need people who really want to be a part of this.  I'm going to try finishing up a test app I have been working on with Django but I should be able to recycle a lot of it to do this."

## First Run
```
cd ~
mkdir Development
cd Development
git clone https://github.com/jake32321/SalukiLAN_Django_Base

sudo pip install virtualenv virtualenvwrapper Django==1.6.5
cd SalukiLAN_Django_Base/Django_App/
virtualenv .
source bin/activate

sudo pip install south

export VIRTUAL_ENV="$HOME/Development/SalukiLAN_Django_Base/Django_App"
export PATH="$HOME/Development/SalukiLAN_Django_Base/Django_App/bin:$PATH"
```

## Usage
`python src/manage.py runserver`
