# Generated by Django 4.0.1 on 2022-01-08 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0009_alter_question_sort_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logicalstring',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
