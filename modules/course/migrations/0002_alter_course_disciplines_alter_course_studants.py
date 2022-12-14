# Generated by Django 4.1.1 on 2022-09-26 17:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='disciplines',
            field=models.ManyToManyField(related_name='courses', to='course.discipline'),
        ),
        migrations.AlterField(
            model_name='course',
            name='studants',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
