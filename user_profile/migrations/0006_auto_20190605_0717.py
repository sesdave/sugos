# Generated by Django 2.2 on 2019-06-05 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_auto_20190605_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='cover',
            field=models.ImageField(default=None, null=True, upload_to='photos/'),
        ),
    ]
