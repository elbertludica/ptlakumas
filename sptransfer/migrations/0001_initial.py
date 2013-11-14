# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Transfer'
        db.create_table(u'sptransfer_transfer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('request_approv', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('request_reject', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cancel_flag', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('closed_flag', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('memo', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'sptransfer', ['Transfer'])

        # Adding model 'TransferItems'
        db.create_table(u'sptransfer_transferitems', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('transfer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sptransfer.Transfer'], on_delete=models.PROTECT)),
            ('origin', self.gf('django.db.models.fields.related.ForeignKey')(related_name='origin', on_delete=models.PROTECT, to=orm['sp_spareparts.StockSpareParts'])),
            ('destination', self.gf('django.db.models.fields.related.ForeignKey')(related_name='destination', on_delete=models.PROTECT, to=orm['sp_spareparts.StockSpareParts'])),
            ('requested_quantity', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('approved_quantity', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('memo', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'sptransfer', ['TransferItems'])

        # Adding model 'TransferItemsDelivery'
        db.create_table(u'sptransfer_transferitemsdelivery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('transfer_items', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sptransfer.TransferItems'], on_delete=models.PROTECT)),
            ('delivery_date', self.gf('django.db.models.fields.DateField')()),
            ('delivered_quantity', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('memo', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'sptransfer', ['TransferItemsDelivery'])


    def backwards(self, orm):
        # Deleting model 'Transfer'
        db.delete_table(u'sptransfer_transfer')

        # Deleting model 'TransferItems'
        db.delete_table(u'sptransfer_transferitems')

        # Deleting model 'TransferItemsDelivery'
        db.delete_table(u'sptransfer_transferitemsdelivery')


    models = {
        u'basicinfo.department': {
            'Meta': {'object_name': 'Department'},
            'department_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'basicinfo.factory': {
            'Meta': {'object_name': 'Factory'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'code_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'basicinfo.machinetype': {
            'Meta': {'object_name': 'MachineType'},
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['basicinfo.Department']", 'on_delete': 'models.PROTECT'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machine_type': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        u'sp_spareparts.masterspareparts': {
            'Meta': {'object_name': 'MasterSpareParts'},
            'barcode': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'chain_wheel_type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'character': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '8'}),
            'lifetime': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'machine_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['basicinfo.MachineType']", 'on_delete': 'models.PROTECT'}),
            'movability': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'natural_frequency': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'spareparts_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sp_spareparts.SparePartsTypes']", 'on_delete': 'models.PROTECT'}),
            'supplier_code': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'sp_spareparts.sparepartstypes': {
            'Meta': {'object_name': 'SparePartsTypes'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'spareparts_type': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        u'sp_spareparts.stockspareparts': {
            'Meta': {'object_name': 'StockSpareParts'},
            'factory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['basicinfo.Factory']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial_quantity': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'master_spare_parts': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sp_spareparts.MasterSpareParts']"}),
            'quantity': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'sptransfer.transfer': {
            'Meta': {'object_name': 'Transfer'},
            'cancel_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'closed_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'memo': ('django.db.models.fields.TextField', [], {}),
            'number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'request_approv': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'request_reject': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'sptransfer.transferitems': {
            'Meta': {'object_name': 'TransferItems'},
            'approved_quantity': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'destination': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'destination'", 'on_delete': 'models.PROTECT', 'to': u"orm['sp_spareparts.StockSpareParts']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'memo': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'origin': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'origin'", 'on_delete': 'models.PROTECT', 'to': u"orm['sp_spareparts.StockSpareParts']"}),
            'requested_quantity': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'transfer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sptransfer.Transfer']", 'on_delete': 'models.PROTECT'})
        },
        u'sptransfer.transferitemsdelivery': {
            'Meta': {'object_name': 'TransferItemsDelivery'},
            'delivered_quantity': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'delivery_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'memo': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'transfer_items': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sptransfer.TransferItems']", 'on_delete': 'models.PROTECT'})
        }
    }

    complete_apps = ['sptransfer']