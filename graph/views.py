# Create your views here.
import pydot
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from graph.models import Graph, Edge, Node

@login_required
def graphs_all(request, flash=[]):
	g = Graph.objects.all()	
	return render(request, 'graph/graph_index.html', { 'graphs':g, 'flash':flash })


@login_required
def graph_by_id(request, g_id):
	mydict = {}
	
	try:
		g = Graph.objects.get(pk=g_id)
	except Graph.DoesNotExist:
		messages.error(request, '<b>ERROR:</b> You requested a graph that does not exist!')
		return HttpResponseRedirect('/graph')

	graph = pydot.Dot(
		graph_name=unicode(g),
		graph_type='digraph')
	
	mydict['graph_name'] = g.name
	
	nodes_qs = g.node_set.all()
	nodes = []
	for n in nodes_qs:
		nodes.append(unicode(n))
		g_n = pydot.Node(
			n.pk, 
			id = unicode(n),
			tooltip = unicode(n),
			label=unicode(n), 
			fontname = 'Helvetica',
			fontsize = 10,
			URL='http://www.nytimes.com/%s' % n.pk)
		graph.add_node(g_n)
		
	if nodes:
		mydict['nodes'] = nodes
	
	edges_qs = g.edge_set.all()
	edges = []
	for e in edges_qs:
		edges.append(unicode(e))
		g_e = pydot.Edge(
			e.source.pk, 
			e.dest.pk, 
			id = unicode(e.source) + '->' + unicode(e.dest),
			tooltip = unicode(e.source) + '->' + unicode(e.dest),
			#label=unicode(e), 
			URL='http://www.wsj.com/%s' % e.pk)
		graph.add_edge(g_e)
	if edges:
		mydict['edges'] = edges
		
	svg = graph.create_svg()
	if (nodes or edges):
		mydict['svg'] = svg

	return render(request, 'graph/graph_by_id.html', mydict)


@login_required
def graph_nodes_all(request, g_id):
	pass