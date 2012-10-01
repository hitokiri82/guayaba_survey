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
        ))
        db.send_create_signal('main', ['Visit'])

        # Adding model 'Question'
        db.create_table('main_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('q_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('canonical', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('main', ['Question'])

        # Adding model 'Question_Text'
        db.create_table('main_question_text', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('locale', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Question'])),
        ))
        db.send_create_signal('main', ['Question_Text'])

        # Adding model 'Option_Text'
        db.create_table('main_option_text', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('locale', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('main', ['Option_Text'])

        # Adding model 'Option'
        db.create_table('main_option', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Question'])),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('canonical', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('main', ['Option'])

        # Adding M2M table for field texts on 'Option'
        db.create_table('main_option_texts', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('option', models.ForeignKey(orm['main.option'], null=False)),
            ('option_text', models.ForeignKey(orm['main.option_text'], null=False))
        ))
        db.create_unique('main_option_texts', ['option_id', 'option_text_id'])

        # Adding model 'Answer'
        db.create_table('main_answer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Visit'])),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Question'])),
            ('text_area', self.gf('django.db.models.fields.TextField')()),
            ('text_field', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('selected', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Option'])),
        ))
        db.send_create_signal('main', ['Answer'])


    def backwards(self, orm):
        # Deleting model 'Visit'
        db.delete_table('main_visit')

        # Deleting model 'Question'
        db.delete_table('main_question')

        # Deleting model 'Question_Text'
        db.delete_table('main_question_text')

        # Deleting model 'Option_Text'
        db.delete_table('main_option_text')

        # Deleting model 'Option'
        db.delete_table('main_option')

        # Removing M2M table for field texts on 'Option'
        db.delete_table('main_option_texts')

        # Deleting model 'Answer'
        db.delete_table('main_answer')


    models = {
        'main.answer': {
            'Meta': {'object_name': 'Answer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Question']"}),
            'selected': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Option']"}),
            'text_area': ('django.db.models.fields.TextField', [], {}),
            'text_field': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Visit']"})
        },
        'main.option': {
            'Meta': {'object_name': 'Option'},
            'canonical': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Question']"}),
            'texts': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['main.Option_Text']", 'symmetrical': 'False'})
        },
        'main.option_text': {
            'Meta': {'object_name': 'Option_Text'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locale': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        'main.question': {
            'Meta': {'object_name': 'Question'},
            'canonical': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'q_type': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'main.question_text': {
            'Meta': {'object_name': 'Question_Text'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locale': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Question']"})
        },
        'main.visit': {
            'Meta': {'object_name': 'Visit'},
            'city': ('django.db.models.fields.TextField', [], {}),
            'country': ('django.db.models.fields.TextField', [], {}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'})
        }
    }

    complete_apps = ['main']