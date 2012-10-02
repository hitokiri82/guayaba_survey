# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Visit.q08'
        db.alter_column('main_visit', 'q08', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'Visit.q02'
        db.alter_column('main_visit', 'q02', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Visit.q03'
        db.alter_column('main_visit', 'q03', self.gf('django.db.models.fields.CharField')(max_length=2, null=True))

        # Changing field 'Visit.q01'
        db.alter_column('main_visit', 'q01', self.gf('django.db.models.fields.CharField')(max_length=2, null=True))

        # Changing field 'Visit.q06'
        db.alter_column('main_visit', 'q06', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Visit.q07'
        db.alter_column('main_visit', 'q07', self.gf('django.db.models.fields.CharField')(max_length=2, null=True))

        # Changing field 'Visit.q04'
        db.alter_column('main_visit', 'q04', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'Visit.q05'
        db.alter_column('main_visit', 'q05', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

    def backwards(self, orm):

        # Changing field 'Visit.q08'
        db.alter_column('main_visit', 'q08', self.gf('django.db.models.fields.CharField')(default='', max_length=1))

        # Changing field 'Visit.q02'
        db.alter_column('main_visit', 'q02', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Visit.q03'
        db.alter_column('main_visit', 'q03', self.gf('django.db.models.fields.CharField')(default='', max_length=2))

        # Changing field 'Visit.q01'
        db.alter_column('main_visit', 'q01', self.gf('django.db.models.fields.CharField')(default='', max_length=2))

        # Changing field 'Visit.q06'
        db.alter_column('main_visit', 'q06', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Visit.q07'
        db.alter_column('main_visit', 'q07', self.gf('django.db.models.fields.CharField')(default='', max_length=2))

        # Changing field 'Visit.q04'
        db.alter_column('main_visit', 'q04', self.gf('django.db.models.fields.CharField')(default='', max_length=1))

        # Changing field 'Visit.q05'
        db.alter_column('main_visit', 'q05', self.gf('django.db.models.fields.CharField')(default='', max_length=1))

    models = {
        'main.contact': {
            'Meta': {'object_name': 'Contact'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'main.visit': {
            'Meta': {'object_name': 'Visit'},
            'city': ('django.db.models.fields.TextField', [], {}),
            'country': ('django.db.models.fields.TextField', [], {}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'q01': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'q02': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'q03': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'q04': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'q05': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'q06': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'q07': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'q08': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'q09': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main']