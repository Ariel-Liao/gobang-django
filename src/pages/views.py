from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	#return HttpResponse("<h1> Hello Pig</h1>") #string of HTML code
	return render(request, "home.html", {})



def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
	mycontext = {
	    "mytext" : "this is so annoying",
	    "mynumer" : 9191,
	    "my_list": [12, 34,23]
	}
	return render(request, "about.html", mycontext)
