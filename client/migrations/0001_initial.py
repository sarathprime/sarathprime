# Generated by Django 4.0.2 on 2022-10-29 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=150)),
                ('contact', models.CharField(max_length=150, null=True)),
            ],
        ),
    ]
