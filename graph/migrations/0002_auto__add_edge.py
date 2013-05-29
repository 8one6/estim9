# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Edge'
        db.create_table(u'graph_edge', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('graph', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['graph.Graph'])),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(related_name='edge_source', to=orm['graph.Node'])),
            ('dest', self.gf('django.db.models.fields.related.ForeignKey')(related_name='edge_dest', to=orm['graph.Node'])),
            ('created', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'graph', ['Edge'])


    def backwards(self, orm):
        # Deleting model 'Edge'
        db.delete_table(u'graph_edge')


    models = {
        u'graph.edge': {
            'Meta': {'object_name': 'Edge'},
            'created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'dest': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'edge_dest'", 'to': u"orm['graph.Node']"}),
            'graph': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['graph.Graph']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'edge_source'", 'to': u"orm['graph.Node']"}),
            'updated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'graph.graph': {
            'Meta': {'object_name': 'Graph'},
            'created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'graph.node': {
            'Meta': {'object_name': 'Node'},
            'created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'graph': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['graph.Graph']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['graph']