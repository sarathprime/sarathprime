# Generated by Django 4.0.2 on 2022-11-18 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='technical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yourname', models.CharField(max_length=150)),
                ('username', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=150)),
                ('contact', models.CharField(max_length=150, null=True)),
            ],
        ),
    ]
