# Generated by Django 4.0.1 on 2022-01-10 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0019_difinedlabel_sort_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='evalabel',
            name='sort_order',
            field=models.CharField(default=0, max_length=3),
        ),
    ]