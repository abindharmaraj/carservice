# Generated by Django 3.0.3 on 2020-05-13 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_log'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=30)),
                ('file', models.CharField(max_length=60)),
            ],
        ),
        migrations.DeleteModel(
            name='admin',
        ),
    ]
