# Generated by Django 4.2.4 on 2023-09-03 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
