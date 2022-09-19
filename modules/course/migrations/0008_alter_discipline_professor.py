# Generated by Django 4.1.1 on 2022-09-19 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0007_alter_discipline_professor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discipline',
            name='professor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='disciplines', to=settings.AUTH_USER_MODEL),
        ),
    ]
