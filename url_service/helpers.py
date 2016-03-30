from django.http import HttpResponse

def HTML_http_response(status_code, HTML_body):
	return HttpResponse(
		content = HTML_body,
		content_type = "text/html",
		status = status_code
	)