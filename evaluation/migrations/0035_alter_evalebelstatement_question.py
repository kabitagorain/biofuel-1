# Generated by Django 4.0.1 on 2022-01-12 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0034_difinedlabel_common_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evalebelstatement',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='evaluation.question'),
        ),
    ]
