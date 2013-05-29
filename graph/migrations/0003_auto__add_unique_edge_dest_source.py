# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Edge', fields ['dest', 'source']
        db.create_unique(u'graph_edge', ['dest_id', 'source_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Edge', fields ['dest', 'source']
        db.delete_unique(u'graph_edge', ['dest_id', 'source_id'])


    models = {
        u'graph.edge': {
            'Meta': {'unique_together': "(('source', 'dest'),)", 'object_name': 'Edge'},
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