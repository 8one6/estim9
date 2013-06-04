from django.db import models

class Graph(models.Model):
	name			= models.CharField(max_length=200)
	description 	= models.TextField(blank=True)
	created			= models.DateField(auto_now_add=True)
	updated			= models.DateField(auto_now=True)
	
	def __unicode__(self):
		return self.name
	def node_count(self):
		return self.node_set.count()
	def edge_count(self):
		return self.edge_set.count()
	def isolated_nodes(self):
		ns = self.node_set.all()
		ins = [n for n in ns if n.is_isolated()]
		return ins
	def isolated_nodes_count(self):
		return len(self.isolated_nodes())

class Node(models.Model):
	name			= models.CharField(max_length=200)
	description		= models.TextField(blank=True)
	graph			= models.ForeignKey('Graph')
	created			= models.DateField(auto_now_add=True)
	updated			= models.DateField(auto_now=True)
	
	def __unicode__(self):
		return self.name
	
	def is_isolated(self):
		has_as_source = self.edge_source.count()
		has_as_dest = self.edge_dest.count()
		return not bool(has_as_source or has_as_dest)
	is_isolated.boolean = True

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