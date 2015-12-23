# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Join'
        db.create_table(u'joins_join', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('ip_address', self.gf('django.db.models.fields.CharField')(default='127.0.0.1', max_length=120)),
            ('ref_id', self.gf('django.db.models.fields.CharField')(default='Default VALUE', max_length=120)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updates', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'joins', ['Join'])


    def backwards(self, orm):
        # Deleting model 'Join'
        db.delete_table(u'joins_join')


    models = {
        u'joins.join': {
            'Meta': {'object_name': 'Join'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'default': "'127.0.0.1'", 'max_length': '120'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'ref_id': ('django.db.models.fields.CharField', [], {'default': "'Default VALUE'", 'max_length': '120'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updates': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['joins']