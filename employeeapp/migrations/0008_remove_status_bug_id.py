# Generated by Django 3.2.5 on 2021-11-05 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapp', '0007_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='bug_id',
        ),
    ]