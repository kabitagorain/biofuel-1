# Generated by Django 4.0.1 on 2022-01-14 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0041_logicalstring_overall_logicalstring_positive_lslabel'),
    ]

    operations = [
        migrations.AddField(
            model_name='optionset',
            name='option_id',
            field=models.CharField(default=0, max_length=252),
        ),
        migrations.AddField(
            model_name='optionset',
            name='overall',
            field=models.CharField(default=0, max_length=1),
        ),
        migrations.AddField(
            model_name='optionset',
            name='positive',
            field=models.CharField(default=0, max_length=1),
        ),
    ]
