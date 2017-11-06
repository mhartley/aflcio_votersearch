from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .utils import geo_api
from .models import *
from django.contrib.gis import geos
import re

def returnindex(request):
	return render(request, 'home.html')


def legislatorhandle(request):
	if request.POST: ##from home form
		print("##INDEX##")
		zipcode = request.POST.get('zipcode')
		address = request.POST.get('address')
		location = address + ' ' + zipcode
		georesponse = geo_api(location)
		if georesponse['status'] =='OK':
			return showleg(request, georesponse['lat'], georesponse['lng'])
		else:
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
		return error(request)

def vote_table(request, incumbent_id):
	pol = Politician.objects.get(id=incumbent_id)
	votes = Vote.objects.filter(politician_id = incumbent_id)
	print("###processing vote_table function###")
	return render(request, 'show_votes.html', {'pol':pol, 'votes':votes})

def elements(request):
	return render(request, 'elements.html')


def welcomemat(request):
	return render(request, 'welcomemat.html')


def emailinputhandle(request):
	if request.POST:
		capturename = request.POST.get('name');
		captureemail = request.POST.get('email');
		if captureemail:
			i = Capture(name = capturename, email = captureemail)
			try:
				i.save()
			except:
				transaction.rollback()

def error(request):
	return render(request, 'error.html')







