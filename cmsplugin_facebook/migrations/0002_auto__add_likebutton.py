# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'LikeButton'
        db.create_table('cmsplugin_likebutton', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(default=None, max_length=200, null=True, blank=True)),
            ('layout', self.gf('django.db.models.fields.CharField')(default='standard', max_length=50)),
            ('show_faces', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('width', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=None, null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=80)),
            ('verb', self.gf('django.db.models.fields.CharField')(default='like', max_length=50)),
            ('font', self.gf('django.db.models.fields.CharField')(default='verdana', max_length=50)),
            ('color_scheme', self.gf('django.db.models.fields.CharField')(default='light', max_length=50)),
        ))
        db.send_create_signal('cmsplugin_facebook', ['LikeButton'])


    def backwards(self, orm):
        
        # Deleting model 'LikeButton'
        db.delete_table('cmsplugin_likebutton')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '5', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'publisher_is_draft': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True', 'blank': 'True'}),
            'publisher_public': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'publisher_draft'", 'unique': 'True', 'null': 'True', 'to': "orm['cms.CMSPlugin']"}),
            'publisher_state': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'cms_facebook.facebookpage': {
            'Meta': {'object_name': 'FacebookPage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pageid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'})
        },
        'cms_facebook.likebox': {
            'Meta': {'object_name': 'LikeBox', 'db_table': "'cmsplugin_likebox'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'connections': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '10'}),
            'header': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '587'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'like_boxes'", 'to': "orm['cms_facebook.FacebookPage']"}),
            'stream': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        'cms_facebook.likebutton': {
            'Meta': {'object_name': 'LikeButton', 'db_table': "'cmsplugin_likebutton'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'color_scheme': ('django.db.models.fields.CharField', [], {'default': "'light'", 'max_length': '50'}),
            'font': ('django.db.models.fields.CharField', [], {'default': "'verdana'", 'max_length': '50'}),
            'height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '80'}),
            'layout': ('django.db.models.fields.CharField', [], {'default': "'standard'", 'max_length': '50'}),
            'show_faces': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'verb': ('django.db.models.fields.CharField', [], {'default': "'like'", 'max_length': '50'}),
            'width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['cms_facebook']
