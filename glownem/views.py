from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core import serializers

from movies.helpers import locations_in_bounds

def home(request):
	return render_to_response('home.html')

def get(request):
	sw_lat  = float(request.GET.get('slat', ''))
	sw_lon =  float(request.GET.get('slon', ''))
	ne_lat  = request.GET.get('nlat', '')
	ne_lon = float(request.GET.get('nlon', ''))

	locs = locations_in_bounds(sw_lat, sw_lon, ne_lat, ne_lon)
	data = serializers.serialize('json', locs)

	return HttpResponse(
        data,
        content_type = 'application/javascript; charset=utf8'
    )