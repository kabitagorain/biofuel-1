# Generated by Django 4.0.1 on 2022-01-14 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0045_rename_option_id_optionset_ls_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='evalebelstatement',
            name='assesment',
            field=models.BooleanField(default=False),
        ),
    ]
