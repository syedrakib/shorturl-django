from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .helpers import HTML_http_response, generate_random_string, is_valid_URL
from .models import URLMapper

# Create your views here.
def index(request):
	if request.method == "GET":
		return render(
			request=request, 
			template_name='shortener_form.html'
		)
	elif request.method == "POST":
		long_url = request.POST['long_url'].strip()
		if not is_valid_URL(long_url):
			return render(
				request=request, 
				template_name='shortener_form.html', 
				status=400,
			)
		else:
			try:
				# if this long_url is alrady present in our DB, we won't create another short URL for it
				urlmapper_obj = URLMapper.objects.get(long_url=long_url)
			except URLMapper.DoesNotExist:
				created = False
				while not created:
					# In highly improbable / unlikely cases,
					# if our generated random string collides with an already existing short_url in DB,
					# we will keep retrying until get_or_create() returns created=True
					urlmapper_obj, created = URLMapper.objects.get_or_create(
						short_url=generate_random_string(7),
						defaults={
							'long_url': long_url
						}
					)
			return HttpResponseRedirect(
				reverse('url_service:inflate', args=(urlmapper_obj.short_url,))
			)
	else:
		return HTML_http_response(200, "<b>restricted attempt</b>")

def redirect(request, short_url):
	return HTML_http_response(200, "<b>redirect %s</b>" % short_url)

def inflate(request, short_url):
	return HTML_http_response(200, "<b>inflate %s</b>" % short_url)
