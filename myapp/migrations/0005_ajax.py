# Generated by Django 3.0.3 on 2020-05-25 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20200513_0945'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ajax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=80)),
                ('password', models.BigIntegerField()),
            ],
        ),
    ]
