from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .utils import geo_api
from .models import *
from django.contrib.gis import geos

def returnindex(request):
	if request.POST: ##from home form
		zipcode = request.POST.get('zipcode')
		address = request.POST.get('address')
		location = address + ' ' + zipcode
		georesponse = geo_api(location)
		if georesponse['status'] =='OK':
			return showleg(request, georesponse['lat'], georesponse['lng'])
		else:
			return HttpResponse('There was an error')
	else:	
		return render(request, 'home.html')

def showleg(request, lat, lng):
	print(lat)
	print(lng)
	user_pt = geos.Point(lng, lat, srid=4326)
	sd = SenateDistrict.objects.get(geom__intersects=user_pt)
	hd = HouseDistrict.objects.get(geom__intersects=user_pt)
	houserep = hd.incumbent
	senrep = sd.incumbent
	string = 'HouseDistrict: %s controlled %s, SenateDistrict %s controlled %s in %s ' % (hd.district, hd.party, sd.district, sd.party, hd.city)
	return render(request, 'showleg.html', {'sd': sd, 'hd': hd, 'houserep': houserep, 'senrep':senrep})


