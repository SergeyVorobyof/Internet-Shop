# Generated by Django 2.0.9 on 2018-12-11 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_auto_20181211_1416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bucket',
            name='num_of_products',
        ),
        migrations.AlterField(
            model_name='bucket',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bucket', to='blog.Order'),
        ),
    ]
