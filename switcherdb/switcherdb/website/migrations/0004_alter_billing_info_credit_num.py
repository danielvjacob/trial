# Generated by Django 4.0.5 on 2022-06-08 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_billing_info_remove_users_billing_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing_info',
            name='credit_num',
            field=models.IntegerField(max_length=16),
        ),
    ]
