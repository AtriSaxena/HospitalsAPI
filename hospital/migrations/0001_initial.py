# Generated by Django 3.0.6 on 2020-05-16 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospitals',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=75)),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('medicine', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('website', models.CharField(blank=True, max_length=100, null=True)),
                ('specilization', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
