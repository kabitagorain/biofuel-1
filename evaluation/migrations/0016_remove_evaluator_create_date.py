# Generated by Django 4.0.1 on 2022-01-09 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0015_alter_evaluator_create_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluator',
            name='create_date',
        ),
    ]
