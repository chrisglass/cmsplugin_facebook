# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'FacebookPage'
        db.create_table('cms_facebook_facebookpage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('pageid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
        ))
        db.send_create_signal('cms_facebook', ['FacebookPage'])

        # Adding model 'LikeBox'
        db.create_table('cmsplugin_likebox', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(related_name='like_boxes', to=orm['cms_facebook.FacebookPage'])),
            ('width', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=None, null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=587)),
            ('connections', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=10)),
            ('stream', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('header', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
        ))
        db.send_create_signal('cms_facebook', ['LikeBox'])


    def backwards(self, orm):
        
        # Deleting model 'FacebookPage'
        db.delete_table('cms_facebook_facebookpage')

        # Deleting model 'LikeBox'
        db.delete_table('cmsplugin_likebox')


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
        }
    }

    complete_apps = ['cms_facebook']
