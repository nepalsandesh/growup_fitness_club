# Generated by Django 4.0.6 on 2022-07-29 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_alter_packagedetails_package_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='admission_charge',
            field=models.FloatField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender'), ('Other', 'Other')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='gym_experience',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='refered_by',
            field=models.CharField(blank=True, choices=[('Social Media', 'Social Media'), ('Friends', 'Friends'), ('Others', 'Others')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='packagedetails',
            name='invoice_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='packagedetails',
            name='package_period',
            field=models.CharField(choices=[('Per Day', 'Per Day'), ('Per Week', 'Per Week'), ('Per Month', 'Per Month'), ('1 Month', '1 Month'), ('3 Months', '3 Months'), ('6 Months', '6 Months'), ('1 Year', '1 Year')], max_length=20),
        ),
        migrations.AlterField(
            model_name='packagedetails',
            name='payment_mode',
            field=models.CharField(blank=True, choices=[('Cash', 'Cash'), ('FonePay', 'FonePay')], max_length=50),
        ),
        migrations.AlterField(
            model_name='packagedetails',
            name='receipt_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='packagedetails',
            name='receipt_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='packagedetails',
            name='received_amount',
            field=models.FloatField(blank=True, default=0, help_text='In Rupees', null=True),
        ),
    ]