# Generated by Django 5.0.6 on 2024-06-28 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0004_orders_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='amountpaid',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='oid',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='paymentstatus',
        ),
    ]
