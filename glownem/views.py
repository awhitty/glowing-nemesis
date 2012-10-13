from django.shortcuts import render_to_response
# from movies.helpers import nearby_locations

def home(request):
	return render_to_response('home.html')

# def get(request):
# 	sw_latitude = request.GET.get('slat', '')
# 	sw_longitude = request.GET.get('slon', '')
# 	ne_latitude = request.GET.get('nlat', '')
# 	ne_longitude = request.GET.get('nlon', '')

# 	