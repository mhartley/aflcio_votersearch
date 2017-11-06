from django.contrib.gis.db import models

class Politician(models.Model):
	lastname = models.CharField(max_length=255)
	firstname = models.CharField(max_length=255)
	photolink = models.CharField(max_length=255)
	grade = models.CharField(max_length=255)
	endorse = models.NullBooleanField(max_length=255)

class District(models.Model):
	district = models.CharField(max_length=255)
	gid = models.IntegerField(primary_key=True)
	geom = models.MultiPolygonField()
	incumbent = models.ForeignKey('Politician', related_name='district')
	city = models.CharField(max_length=255, null=True)
	party = models.CharField(max_length=255, null=True)
	chamber = models.CharField(max_length=10, null=True)

class Bill(models.Model):
	billname = models.CharField(max_length=255)
	description = models.CharField(max_length=500)

class Vote(models.Model):
	politician = models.ForeignKey('Politician')
	bill = models.ForeignKey(Bill, related_name='hvote')
	unionvote = models.BooleanField()

class Capture(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField()







