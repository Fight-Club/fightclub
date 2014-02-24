# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Fighter.url'
        db.delete_column(u'whowin_fighter', 'url')


    def backwards(self, orm):
        # Adding field 'Fighter.url'
        db.add_column(u'whowin_fighter', 'url',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200),
                      keep_default=False)


    models = {
        u'whowin.fight': {
            'Meta': {'object_name': 'Fight'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fighter_1'", 'to': u"orm['whowin.Fighter']"}),
            'member2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fighter_2'", 'to': u"orm['whowin.Fighter']"})
        },
        u'whowin.fighter': {
            'Meta': {'object_name': 'Fighter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rating': ('django.db.models.fields.DecimalField', [], {'default': '1600', 'max_digits': '8', 'decimal_places': '2'})
        }
    }

    complete_apps = ['whowin']