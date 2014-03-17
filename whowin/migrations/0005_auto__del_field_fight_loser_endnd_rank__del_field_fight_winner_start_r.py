# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Fight.loser_endnd_rank'
        db.delete_column(u'whowin_fight', 'loser_endnd_rank')

        # Deleting field 'Fight.winner_start_rank'
        db.delete_column(u'whowin_fight', 'winner_start_rank')

        # Deleting field 'Fight.winner_end_rank'
        db.delete_column(u'whowin_fight', 'winner_end_rank')

        # Deleting field 'Fight.loser_start_rating'
        db.delete_column(u'whowin_fight', 'loser_start_rating')

        # Deleting field 'Fight.loser_start_rank'
        db.delete_column(u'whowin_fight', 'loser_start_rank')

        # Deleting field 'Fight.winner_start_rating'
        db.delete_column(u'whowin_fight', 'winner_start_rating')

        # Deleting field 'Fight.winner_end_rating'
        db.delete_column(u'whowin_fight', 'winner_end_rating')

        # Deleting field 'Fight.loser_end_rating'
        db.delete_column(u'whowin_fight', 'loser_end_rating')

        # Adding field 'Fight.member1_start_rank'
        db.add_column(u'whowin_fight', 'member1_start_rank',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Fight.member1_end_rank'
        db.add_column(u'whowin_fight', 'member1_end_rank',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Fight.member1_start_rating'
        db.add_column(u'whowin_fight', 'member1_start_rating',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Fight.member1_end_rating'
        db.add_column(u'whowin_fight', 'member1_end_rating',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Fight.member2_start_rank'
        db.add_column(u'whowin_fight', 'member2_start_rank',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Fight.member2_endnd_rank'
        db.add_column(u'whowin_fight', 'member2_endnd_rank',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Fight.member2_start_rating'
        db.add_column(u'whowin_fight', 'member2_start_rating',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Fight.member2_end_rating'
        db.add_column(u'whowin_fight', 'member2_end_rating',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Fight.loser_endnd_rank'
        db.add_column(u'whowin_fight', 'loser_endnd_rank',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Fight.winner_start_rank'
        db.add_column(u'whowin_fight', 'winner_start_rank',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Fight.winner_end_rank'
        db.add_column(u'whowin_fight', 'winner_end_rank',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Fight.loser_start_rating'
        db.add_column(u'whowin_fight', 'loser_start_rating',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Fight.loser_start_rank'
        db.add_column(u'whowin_fight', 'loser_start_rank',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Fight.winner_start_rating'
        db.add_column(u'whowin_fight', 'winner_start_rating',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Fight.winner_end_rating'
        db.add_column(u'whowin_fight', 'winner_end_rating',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Fight.loser_end_rating'
        db.add_column(u'whowin_fight', 'loser_end_rating',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True),
                      keep_default=False)

        # Deleting field 'Fight.member1_start_rank'
        db.delete_column(u'whowin_fight', 'member1_start_rank')

        # Deleting field 'Fight.member1_end_rank'
        db.delete_column(u'whowin_fight', 'member1_end_rank')

        # Deleting field 'Fight.member1_start_rating'
        db.delete_column(u'whowin_fight', 'member1_start_rating')

        # Deleting field 'Fight.member1_end_rating'
        db.delete_column(u'whowin_fight', 'member1_end_rating')

        # Deleting field 'Fight.member2_start_rank'
        db.delete_column(u'whowin_fight', 'member2_start_rank')

        # Deleting field 'Fight.member2_endnd_rank'
        db.delete_column(u'whowin_fight', 'member2_endnd_rank')

        # Deleting field 'Fight.member2_start_rating'
        db.delete_column(u'whowin_fight', 'member2_start_rating')

        # Deleting field 'Fight.member2_end_rating'
        db.delete_column(u'whowin_fight', 'member2_end_rating')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'whowin.fight': {
            'Meta': {'object_name': 'Fight'},
            'end': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loser': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'loser'", 'null': 'True', 'to': u"orm['whowin.Fighter']"}),
            'member1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fighter_1'", 'to': u"orm['whowin.Fighter']"}),
            'member1_end_rank': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'member1_end_rating': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'member1_start_rank': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'member1_start_rating': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'member2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fighter_2'", 'to': u"orm['whowin.Fighter']"}),
            'member2_end_rating': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'member2_endnd_rank': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'member2_start_rank': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'member2_start_rating': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'winner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'winner'", 'null': 'True', 'to': u"orm['whowin.Fighter']"})
        },
        u'whowin.fighter': {
            'Meta': {'object_name': 'Fighter'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'fightslost': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fightswon': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rating': ('django.db.models.fields.DecimalField', [], {'default': '1600', 'max_digits': '8', 'decimal_places': '2'}),
            'side': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': '0', 'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['whowin']