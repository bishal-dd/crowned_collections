# Generated by Django 3.1.7 on 2021-03-17 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20210317_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product_name',
            field=models.CharField(max_length=100),
        ),
    ]
