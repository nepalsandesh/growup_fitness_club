# Generated by Django 4.0.6 on 2022-07-27 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_alter_member_member_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagedetails',
            name='convenient_time',
            field=models.CharField(blank=True, choices=[('Morning', 'Morning'), ('Evening', 'Evening')], max_length=20),
        ),
        migrations.AlterField(
            model_name='packagedetails',
            name='package_period',
            field=models.CharField(choices=[('Per Day', '1 Day'), ('Per Week', '1 Week'), ('Per Month', '1 Month'), ('1 month', '1 Month'), ('3 months', '3 Months'), ('6 months', '6 Months'), ('1 year', '1 Year')], max_length=20),
        ),
        migrations.AlterField(
            model_name='packagedetails',
            name='payment_mode',
            field=models.CharField(blank=True, choices=[('Cash', 'Cash'), ('Fonepay', 'Fonepay')], max_length=50),
        ),
    ]
