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
	node_src		= models.ForeignKey('Node', related_name='node_src')
	node_dest		= models.ForeignKey('Node', related_name='node_dest')
	created			= models.DateField(auto_now_add=True)
	updated			= models.DateField(auto_now=True)
	def __unicode__(self):
		if self.name:
			return u'%s: %s->%s' % (self.name, self.node_src, self.node_dest)
		else:
			return u'%s->%s' % (self.node_src, self.node_dest)
	class Meta:
		unique_together = ((node_src, node_dest,),)
		