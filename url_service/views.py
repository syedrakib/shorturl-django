from django.http import HttpResponse
from django.shortcuts import render
from .helpers import HTML_http_response

# Create your views here.
def index(request):
	if request.method == "GET":
		return render(
			request=request, 
			template_name='shortener_form.html'
		)
	elif request.method == "POST":
		return HTML_http_response(200, "<b>process form</b>")
	else:
		return HTML_http_response(200, "<b>restricted attempt</b>")

def redirect(request, short_url):
	return HTML_http_response(200, "<b>redirect %s</b>" % short_url)

def inflate(request, short_url):
	return HTML_http_response(200, "<b>inflate %s</b>" % short_url)
