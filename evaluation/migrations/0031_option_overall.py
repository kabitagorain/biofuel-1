# Generated by Django 4.0.1 on 2022-01-11 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0030_evalebelstatement_evaluator'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='overall',
            field=models.CharField(default=0, max_length=1),
        ),
    ]
