# Generated by Django 2.2.28 on 2023-08-02 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value3', models.BigIntegerField()),
                ('value4', models.ImageField(blank=True, null=True, upload_to='test3/value4/images/')),
                ('value5', models.CharField(blank=True, max_length=255, null=True)),
                ('value6', models.PositiveIntegerField(blank=True, null=True)),
                ('value877', models.TimeField(blank=True, null=True)),
                ('value8', models.SmallIntegerField(blank=True, null=True)),
                ('value9', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
