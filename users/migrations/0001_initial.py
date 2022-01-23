# Generated by Django 2.2 on 2022-01-23 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vegetables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_id', models.CharField(max_length=20)),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=150)),
            ],
        ),
    ]
