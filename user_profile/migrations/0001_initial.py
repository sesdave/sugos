# Generated by Django 2.2 on 2019-06-04 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_thumbs.fields
import user_profile.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_thumbs.fields.ImageThumbsField(blank=True, default=None, null=True, sizes=({'code': '60x60', 'resize': 'crop', 'wxh': '60x60'}, {'code': '100x100', 'resize': 'crop', 'wxh': '100x100'}, {'code': '200x200', 'resize': 'crop', 'wxh': '200x200'}, {'code': '400x400', 'resize': 'crop', 'wxh': '400x400'}), upload_to=user_profile.models.upload_avatar_to)),
                ('bio', models.TextField(blank=True, default=None, max_length=500, null=True, verbose_name='Write about your self')),
                ('location', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('rc_number', models.CharField(default=None, max_length=60)),
                ('company_name', models.CharField(blank=True, default=None, max_length=60, null=True)),
                ('website', models.CharField(blank=True, default=None, max_length=60, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
