# Generated by Django 2.0.9 on 2018-12-09 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20181209_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.IntegerField(default=1, primary_key=True),
        ),
    ]