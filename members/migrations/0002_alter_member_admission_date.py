# Generated by Django 4.0.6 on 2022-07-29 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='admission_date',
            field=models.DateField(null=True),
        ),
    ]
