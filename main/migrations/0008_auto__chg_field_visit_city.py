# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Visit.city'
        db.alter_column('main_visit', 'city', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

    def backwards(self, orm):

        # Changing field 'Visit.city'
        db.alter_column('main_visit', 'city', self.gf('django.db.models.fields.TextField')(max_length=50, null=True))

    models = {
        'main.contact': {
            'Meta': {'object_name': 'Contact'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'main.visit': {
            'Meta': {'object_name': 'Visit'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'q01': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'q02': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'q03': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'q04': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'q05': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'q06': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'q07': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'q08': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'q09': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'q10': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '2083', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main']