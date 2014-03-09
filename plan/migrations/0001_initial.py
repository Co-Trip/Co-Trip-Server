# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Plan'
        db.create_table(u'plan_plan', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('home_city', self.gf('django.db.models.fields.related.ForeignKey')(related_name='home_city_plan_set', to=orm['cities_light.City'])),
            ('leaving_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('return_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('leaving_transportation', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('return_transportation', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('participants_number', self.gf('django.db.models.fields.IntegerField')()),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='create_plan_set', to=orm['traveller.Traveller'])),
            ('is_public', self.gf('django.db.models.fields.BooleanField')()),
            ('participants_can_edit', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'plan', ['Plan'])

        # Adding M2M table for field destination_city on 'Plan'
        m2m_table_name = db.shorten_name(u'plan_plan_destination_city')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('plan', models.ForeignKey(orm[u'plan.plan'], null=False)),
            ('city', models.ForeignKey(orm[u'cities_light.city'], null=False))
        ))
        db.create_unique(m2m_table_name, ['plan_id', 'city_id'])

        # Adding M2M table for field participants on 'Plan'
        m2m_table_name = db.shorten_name(u'plan_plan_participants')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('plan', models.ForeignKey(orm[u'plan.plan'], null=False)),
            ('traveller', models.ForeignKey(orm[u'traveller.traveller'], null=False))
        ))
        db.create_unique(m2m_table_name, ['plan_id', 'traveller_id'])

        # Adding model 'Site'
        db.create_table(u'plan_site', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('daily_plan', self.gf('django.db.models.fields.related.ForeignKey')(related_name='daily_site_set', null=True, to=orm['plan.DailyPlan'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('spend', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal(u'plan', ['Site'])

        # Adding M2M table for field up_voters on 'Site'
        m2m_table_name = db.shorten_name(u'plan_site_up_voters')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('site', models.ForeignKey(orm[u'plan.site'], null=False)),
            ('traveller', models.ForeignKey(orm[u'traveller.traveller'], null=False))
        ))
        db.create_unique(m2m_table_name, ['site_id', 'traveller_id'])

        # Adding M2M table for field down_voters on 'Site'
        m2m_table_name = db.shorten_name(u'plan_site_down_voters')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('site', models.ForeignKey(orm[u'plan.site'], null=False)),
            ('traveller', models.ForeignKey(orm[u'traveller.traveller'], null=False))
        ))
        db.create_unique(m2m_table_name, ['site_id', 'traveller_id'])

        # Adding model 'Meal'
        db.create_table(u'plan_meal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('meal_type', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('daily_plan', self.gf('django.db.models.fields.related.ForeignKey')(related_name='meal_set', to=orm['plan.DailyPlan'])),
        ))
        db.send_create_signal(u'plan', ['Meal'])

        # Adding model 'SiteImage'
        db.create_table(u'plan_siteimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(related_name='site_image_set', to=orm['plan.Site'])),
        ))
        db.send_create_signal(u'plan', ['SiteImage'])

        # Adding model 'DailyPlan'
        db.create_table(u'plan_dailyplan', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('day_number', self.gf('django.db.models.fields.IntegerField')()),
            ('hotel', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('transportation', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('primary_plan', self.gf('django.db.models.fields.related.ForeignKey')(related_name='daily_plan_set', to=orm['plan.Plan'])),
        ))
        db.send_create_signal(u'plan', ['DailyPlan'])


    def backwards(self, orm):
        # Deleting model 'Plan'
        db.delete_table(u'plan_plan')

        # Removing M2M table for field destination_city on 'Plan'
        db.delete_table(db.shorten_name(u'plan_plan_destination_city'))

        # Removing M2M table for field participants on 'Plan'
        db.delete_table(db.shorten_name(u'plan_plan_participants'))

        # Deleting model 'Site'
        db.delete_table(u'plan_site')

        # Removing M2M table for field up_voters on 'Site'
        db.delete_table(db.shorten_name(u'plan_site_up_voters'))

        # Removing M2M table for field down_voters on 'Site'
        db.delete_table(db.shorten_name(u'plan_site_down_voters'))

        # Deleting model 'Meal'
        db.delete_table(u'plan_meal')

        # Deleting model 'SiteImage'
        db.delete_table(u'plan_siteimage')

        # Deleting model 'DailyPlan'
        db.delete_table(u'plan_dailyplan')


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
        u'cities_light.city': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('region', 'name'),)", 'object_name': 'City'},
            'alternate_names': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Country']"}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'feature_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'population': ('django.db.models.fields.BigIntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Region']", 'null': 'True', 'blank': 'True'}),
            'search_names': ('cities_light.models.ToSearchTextField', [], {'default': "''", 'max_length': '4000', 'db_index': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"})
        },
        u'cities_light.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'alternate_names': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'code2': ('django.db.models.fields.CharField', [], {'max_length': '2', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'code3': ('django.db.models.fields.CharField', [], {'max_length': '3', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'continent': ('django.db.models.fields.CharField', [], {'max_length': '2', 'db_index': 'True'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"}),
            'tld': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '5', 'blank': 'True'})
        },
        u'cities_light.region': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('country', 'name'),)", 'object_name': 'Region'},
            'alternate_names': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Country']"}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'geoname_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'plan.dailyplan': {
            'Meta': {'object_name': 'DailyPlan'},
            'day_number': ('django.db.models.fields.IntegerField', [], {}),
            'hotel': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'primary_plan': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'daily_plan_set'", 'to': u"orm['plan.Plan']"}),
            'transportation': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'plan.meal': {
            'Meta': {'object_name': 'Meal'},
            'daily_plan': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'meal_set'", 'to': u"orm['plan.DailyPlan']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meal_type': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'plan.plan': {
            'Meta': {'object_name': 'Plan'},
            'create_time': ('django.db.models.fields.DateTimeField', [], {}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'create_plan_set'", 'to': u"orm['traveller.Traveller']"}),
            'destination_city': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'destination_city_set'", 'symmetrical': 'False', 'to': u"orm['cities_light.City']"}),
            'home_city': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'home_city_plan_set'", 'to': u"orm['cities_light.City']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {}),
            'leaving_date': ('django.db.models.fields.DateTimeField', [], {}),
            'leaving_transportation': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'participants': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'participate_plan_set'", 'blank': 'True', 'to': u"orm['traveller.Traveller']"}),
            'participants_can_edit': ('django.db.models.fields.BooleanField', [], {}),
            'participants_number': ('django.db.models.fields.IntegerField', [], {}),
            'return_date': ('django.db.models.fields.DateTimeField', [], {}),
            'return_transportation': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'plan.site': {
            'Meta': {'object_name': 'Site'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'daily_plan': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'daily_site_set'", 'null': 'True', 'to': u"orm['plan.DailyPlan']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'down_voters': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'down_voting_plan_set'", 'symmetrical': 'False', 'to': u"orm['traveller.Traveller']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'spend': ('django.db.models.fields.IntegerField', [], {}),
            'up_voters': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'up_voting_plan_set'", 'symmetrical': 'False', 'to': u"orm['traveller.Traveller']"})
        },
        u'plan.siteimage': {
            'Meta': {'object_name': 'SiteImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'site_image_set'", 'to': u"orm['plan.Site']"})
        },
        u'traveller.traveller': {
            'Meta': {'object_name': 'Traveller'},
            'avatar_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.City']", 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'profile'", 'unique': 'True', 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['plan']