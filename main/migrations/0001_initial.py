# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Visit'
        db.create_table('main_visit', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ip_address', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('country', self.gf('django.db.models.fields.TextField')()),
            ('city', self.gf('django.db.models.fields.TextField')()),
            ('q01', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('q02', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('q03', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('q04', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('q05', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('q06', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('q07', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('q08', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('q09', self.gf('django.db.models.fields.IntegerField')(blank=True)),
        ))
        db.send_create_signal('main', ['Visit'])

        # Adding model 'Contact'
        db.create_table('main_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('main', ['Contact'])


    def backwards(self, orm):
        # Deleting model 'Visit'
        db.delete_table('main_visit')

        # Deleting model 'Contact'
        db.delete_table('main_contact')


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
            'q01': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'q02': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'q03': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'q04': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'q05': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'q06': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'q07': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'q08': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'q09': ('django.db.models.fields.IntegerField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['main']