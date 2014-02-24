# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Fighter'
        db.create_table(u'whowin_fighter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('rating', self.gf('django.db.models.fields.DecimalField')(default=1600, max_digits=8, decimal_places=2)),
        ))
        db.send_create_signal(u'whowin', ['Fighter'])

        # Adding model 'Fight'
        db.create_table(u'whowin_fight', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('member1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fighter_1', to=orm['whowin.Fighter'])),
            ('member2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fighter_2', to=orm['whowin.Fighter'])),
        ))
        db.send_create_signal(u'whowin', ['Fight'])


    def backwards(self, orm):
        # Deleting model 'Fighter'
        db.delete_table(u'whowin_fighter')

        # Deleting model 'Fight'
        db.delete_table(u'whowin_fight')


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