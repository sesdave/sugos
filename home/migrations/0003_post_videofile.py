# Generated by Django 2.2 on 2019-06-24 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_usermessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='videofile',
            field=models.FileField(null=True, upload_to='videos/', verbose_name=''),
        ),
    ]