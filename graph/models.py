from django.db import models

class Graph(models.Model):
	name			= models.CharField(max_length=200)
	description 	= models.TextField(blank=True)
	created			= models.DateField(auto_now_add=True)
	updated			= models.DateField(auto_now=True)
	
	def __unicode__(self):
		return self.name

class Node(models.Model):
	name			= models.CharField(max_length=200)
	description		= models.TextField(blank=True)
	graph			= models.ForeignKey('Graph')
	created			= models.DateField(auto_now_add=True)
	updated			= models.DateField(auto_now=True)
	
	def __unicode__(self):
		return self.name

class Edge(models.Model):
	name			= models.CharField(max_length=200, blank=True)
	description		= models.TextField(blank=True)
	graph			= models.ForeignKey('Graph')
	source			= models.ForeignKey('Node', related_name='edge_source')
	dest			= models.ForeignKey('Node', related_name='edge_dest')
	created			= models.DateField(auto_now_add=True)
	updated			= models.DateField(auto_now=True)
	
	class Meta:
		unique_together = (('source', 'dest',),)
	
	def __unicode__(self):
		if self.name:
			return u'%s: %s->%s' % (self.name, self.source, self.dest)
		else:
			return u'%s->%s' % (self.source, self.dest)