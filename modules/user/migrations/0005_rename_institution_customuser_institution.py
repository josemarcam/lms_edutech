# Generated by Django 4.1.1 on 2022-09-26 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_customuser_institution'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='Institution',
            new_name='institution',
        ),
    ]
