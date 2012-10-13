from models import Location

def locations_in_bounds(sw_lat, sw_lon, ne_lat, ne_lon):
	return Location.objects.filter(latitude__gt=sw_lat, latitude__lt=ne_lat, longitude__gt=sw_lon, longitude__lt=ne_lon)