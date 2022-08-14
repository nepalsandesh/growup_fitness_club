# Generated by Django 4.0.6 on 2022-08-14 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='country',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='current_address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='member',
            name='district',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='full_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='member',
            name='local_gov',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='mobile',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='member',
            name='ward_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='packagedetails',
            name='convenient_time',
            field=models.CharField(choices=[('Morning', 'Morning'), ('Evening', 'Evening')], max_length=50),
        ),
        migrations.AlterField(
            model_name='packagedetails',
            name='payment_mode',
            field=models.CharField(choices=[('Cash', 'Cash'), ('FonePay', 'FonePay')], max_length=50),
        ),
    ]
