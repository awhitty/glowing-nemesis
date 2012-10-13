from django.http import HttpResponse
from models import Movie, Location

# Create your views here.

def location(request, lat, long, dx, dy):
	lat = float(lat)
	long = float(long)
	dx = float(dx)
	dy = float(dy)
	
	locations = Location.objects.filter(latitude__range=(lat-dx, lat+dx)).filter(longitude__range=(long-dy,long+dy))
	response = ""
	response += "%f, %f, %f, %f\n" % (lat-dx, lat+dx, long-dy, long+dy)
	for l in locations:
		response += l.movie.name + "<br />\n"
	return HttpResponse(response)
