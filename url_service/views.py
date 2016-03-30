from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
	if request.method == "GET":
		return HTML_http_response(200, "<b>show form</b>")
	elif request.method == "POST":
		return HTML_http_response(200, "<b>process form</b>")
	else:
		return HTML_http_response(200, "<b>restricted attempt</b>")

def redirect(request, short_url):
	return HTML_http_response(200, "<b>redirect %s</b>" % short_url)

def inflate(request, short_url):
	return HTML_http_response(200, "<b>inflate %s</b>" % short_url)

def HTML_http_response(status_code, HTML_body):
	return HttpResponse(
		content = HTML_body,
		content_type = "text/html",
		status = status_code
	)