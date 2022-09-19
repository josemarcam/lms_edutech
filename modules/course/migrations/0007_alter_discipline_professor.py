# Generated by Django 4.1.1 on 2022-09-19 19:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0006_alter_course_disciplines'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discipline',
            name='professor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='disciplines', to=settings.AUTH_USER_MODEL),
        ),
    ]