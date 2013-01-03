# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserCount'
        db.create_table('md_pypispy_users_usercount', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('value', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('md_pypispy_users', ['UserCount'])


    def backwards(self, orm):
        # Deleting model 'UserCount'
        db.delete_table('md_pypispy_users_usercount')


    models = {
        'md_pypispy_users.usercount': {
            'Meta': {'object_name': 'UserCount'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['md_pypispy_users']