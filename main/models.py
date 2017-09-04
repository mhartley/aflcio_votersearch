from django.contrib.gis.db import models

class Politician(models.Model):
	lastname = models.CharField(max_length=255)
	firstname = models.CharField(max_length=255)
	photolink = models.CharField(max_length=255)
	score = models.CharField(max_length=255)

class SenateDistrict(models.Model):
	district = models.CharField(max_length=255)
	gid = models.IntegerField(primary_key=True)
	geom = models.MultiPolygonField()
	incumbent = models.ForeignKey('Politician')
	city = models.CharField(max_length=255, null=True)
	party = models.CharField(max_length=255, null=True)

class HouseDistrict(models.Model):
	district = models.CharField(max_length=255)
	gid = models.IntegerField(primary_key=True)
	geom = models.MultiPolygonField()
	incumbent = models.ForeignKey('Politician')
	city = models.CharField(max_length=255, null=True)
	party = models.CharField(max_length=255, null=True)

class HouseMember(models.Model):
	incumbent = models.ForeignKey('Politician')
	district = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	party = models.CharField(max_length=255)

class Bill(models.Model):
	billname = models.CharField(max_length=255)
	description = models.CharField(max_length=500)

class SenateVotes(models.Model): ## these tables should just be a manay to many field?
	senatemember = models.ForeignKey('Politician')
	bill = models.ForeignKey(Bill)
	unionvote = models.BooleanField()

class HouseVotes(models.Model): ## these tables should just be a manay to many field?
	senateMember = models.ForeignKey('Politician')
	bill = models.ForeignKey('Bill')
	unionvote = models.BooleanField()


#




