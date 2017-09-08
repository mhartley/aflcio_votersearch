from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .utils import geo_api
from .models import *
from django.contrib.gis import geos

def returnindex(request):
	if request.POST: ##from home form
		print("##INDEX##")
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
	sd = District.objects.filter(chamber='s').get(geom__intersects=user_pt)
	hd = District.objects.filter(chamber='h').get(geom__intersects=user_pt)
	houserep = hd.incumbent
	senrep = sd.incumbent
	string = 'HouseDistrict: %s controlled %s, SenateDistrict %s controlled %s in %s ' % (hd.district, hd.party, sd.district, sd.party, hd.city)
	return render(request, 'showleg.html', {'sd': sd, 'hd': hd, 'houserep': houserep, 'senrep':senrep})

def vote_table(request, incumbent_id):
	pol = Politician.objects.get(id=incumbent_id)
	votes = Vote.objects.filter(politician_id = incumbent_id)
	print("###processing vote_table function###")
	return render(request, 'show_votes.html', {'pol':pol, 'votes':votes})

def elements(request):
		return render(request, 'elements.html')
