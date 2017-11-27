from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .utils import geo_api
from .models import *
from django.contrib.gis import geos
import re




##function to return user ip -- does not return a page

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def returnindex(request):
	return render(request, 'home.html', {'error':False})


def legislatorhandle(request):
	if request.POST: ##from home form
		zipcode = request.POST.get('zipcode')
		address = request.POST.get('address')
		email = request.POST.get('email')
		cellphone = request.POST.get('cellphone')
		client_ip = get_client_ip(request)
		##call the google api -- function in utils.py
		location = address + ' ' + zipcode
		georesponse = geo_api(location)
		if georesponse['status'] =='OK':
			#save the form data
			i = Capture(zipcode = zipcode, address = address, email = email, cellphone = cellphone, client_ip = client_ip, georeturn = True)
			try:
				i.save()
			except:
				transaction.rollback()
			#show them the goodies
			return showleg(request, georesponse['lat'], georesponse['lng'])
		else:
			#save the form data
			i = Capture(zipcode = zipcode, address = address, email = email, cellphone = cellphone, client_ip = client_ip, georeturn = False)
			try:
				i.save()
			except:
				transaction.rollback()
			#start fresh from home page with an error message
			return render(request, 'home.html', {'error':True})
	else:
		return render(request, 'home.html', {'error':True})

def showleg(request, lat, lng):
	print(lat)
	print(lng)
	try:
		user_pt = geos.Point(lng, lat, srid=4326)
		sd = District.objects.filter(chamber='s').get(geom__intersects=user_pt)
		hd = District.objects.filter(chamber='h').get(geom__intersects=user_pt)
		cd = District.objects.filter(chamber='c').get(geom__intersects=user_pt)
		houserep = hd.incumbent
		senrep = sd.incumbent
		congrep = cd.incumbent
		print('###$$$$$' + congrep.lastname)
		string = 'HouseDistrict: %s controlled %s, SenateDistrict %s controlled %s in %s ' % (hd.district, hd.party, sd.district, sd.party, hd.city)
		return render(request, 'showleg.html', {'cd': cd, 'sd': sd, 'hd': hd, 'congrep': congrep, 'houserep': houserep, 'senrep':senrep, 'lat':lat, 'lng':lng})
	except:
		return render(request, 'home.html', {'error':True})

def vote_table(request, incumbent_id):
	pol = Politician.objects.get(id=incumbent_id)
	votes = Vote.objects.filter(politician_id = incumbent_id)
	return render(request, 'show_votes.html', {'pol':pol, 'votes':votes})

def elements(request):
	return render(request, 'elements.html')


def welcomemat(request):
	return render(request, 'welcomemat.html')


def error(request):
	return render(request, 'error.html')







