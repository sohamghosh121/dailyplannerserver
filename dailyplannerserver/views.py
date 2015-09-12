from django.http import HttpResponse

def healthCheck(req):
	return HttpResponse('It\'s all good!')

def getLocations(req):
	return HttpResponse('ok')