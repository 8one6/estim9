from django.contrib import admin
from graph.models import Graph, Node, Edge

class EdgeAdmin(admin.ModelAdmin):
	fields = ('graph', ('source', 'dest'), 'name', 'description')
	
admin.site.register(Edge, EdgeAdmin)
admin.site.register(Graph)
admin.site.register(Node)
