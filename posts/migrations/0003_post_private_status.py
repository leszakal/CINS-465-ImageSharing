# Generated by Django 3.0.9 on 2021-05-10 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210510_0457'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='private_status',
            field=models.BooleanField(default=False),
        ),
    ]