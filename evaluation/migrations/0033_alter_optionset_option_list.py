# Generated by Django 4.0.1 on 2022-01-11 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0032_optionset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optionset',
            name='option_list',
            field=models.CharField(max_length=252, unique=True),
        ),
    ]
