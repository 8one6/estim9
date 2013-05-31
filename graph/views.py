# Create your views here.
import pydot
from django.shortcuts import render

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