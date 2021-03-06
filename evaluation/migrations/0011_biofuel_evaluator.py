# Generated by Django 4.0.1 on 2022-01-08 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0010_alter_logicalstring_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biofuel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=252)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=252)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=16)),
                ('orgonization', models.CharField(max_length=252)),
                ('biofuel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='evaluation.biofuel')),
            ],
        ),
    ]
