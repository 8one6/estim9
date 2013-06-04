# Create your views here.
import pydot
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from graph.models import Graph, Edge, Node

@login_required
def graphs_all(request):
	g = Graph.objects.all()	
	return render(request, 'graph/graph_index.html', {'graphs':g})


@login_required
def gvtest(request):
	graph = pydot.Dot(graph_type='graph')
	
	numlords = 3
	numvassalsplord = 3
	for i in range(numlords):
		edge = pydot.Edge("king", "lord%d" % i)
		graph.add_edge(edge)
		
	vassal_num = 0
	for i in range(numlords):
		for j in range(numvassalsplord):
			edge = pydot.Edge("lord%d" % i, "vassal%d" % vassal_num)
			graph.add_edge(edge)
			vassal_num+=1
	
	svg = graph.create_svg()
	mydict = {}
	mydict['content'] = svg
	return render(request, 'base.html', mydict)


@login_required
def gvtest2(request, graph_id=1):
	mydict = {}
	
	graph_qs = Graph.objects.get(pk=graph_id)
	graph = pydot.Dot(
		graph_name=unicode(graph_qs),
		graph_type='digraph')
	
	mydict['graph_name'] = graph_qs.name
	
	nodes_qs = Node.objects.filter(graph=graph_id)
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
	
	edges_qs = Edge.objects.filter(graph=graph_id)
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
	
	return render(request, 'graphview.html', mydict)
