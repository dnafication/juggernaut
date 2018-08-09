# Generated by Django 2.1 on 2018-08-08 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JMX',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('jmxfile', models.FileField(upload_to='jmxes')),
                ('date_added', models.DateTimeField(verbose_name='date added')),
            ],
        ),
    ]
