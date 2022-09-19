# Generated by Django 4.1.1 on 2022-09-08 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('workload', models.IntegerField()),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]