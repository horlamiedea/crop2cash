# Generated by Django 3.1.7 on 2021-04-08 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
