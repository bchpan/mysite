# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Book'
        db.create_table(u'blog_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('book_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'blog', ['Book'])


    def backwards(self, orm):
        # Deleting model 'Book'
        db.delete_table(u'blog_book')


    models = {
        u'blog.book': {
            'Meta': {'object_name': 'Book'},
            'book_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['blog']