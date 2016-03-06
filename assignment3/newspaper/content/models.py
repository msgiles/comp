from __future__ import unicode_literals

from django.db import models
from datetime import datetime

class Content(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    contributors = models.ManyToManyField('Contributor',
                                          related_name='content')
    pub_date = models.DateTimeField('date published')


class Article(Content):
    text = models.TextField()
    def show(self):
    	lst = self.contributors.all().values()
    	contribs = ', '.join(contrib['first_name'] + ' ' + contrib['last_name'] for contrib in lst)
    	r = ["Title: " + self.title, "Subtitle: " + self.subtitle, 
    	"Contributors: " + contribs, "Publication Date: " + 
    	self.pub_date]
    	return '; '.join(r)

class Image(Content):
    path = models.CharField(max_length=500)
    def show(self):
    	lst = self.contributors.all().values()
    	contribs = ', '.join(contrib['first_name'] + ' ' + contrib['last_name'] for contrib in lst)
    	r = ["Title: " + self.title, "Caption: " + self.subtitle, 
    	"Contributors: " + contribs, "Publication Date: " + 
    	self.pub_date]
    	return '; '.join(r)

class Contributor(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    def die(self):
    	self.delete()	
    def __str__(self):
    	return "{} {}".format(self.first_name, self.last_name)
