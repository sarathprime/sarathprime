# Generated by Django 4.0.7 on 2022-11-22 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0010_link_amount_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='link_amount',
            name='targetamount1',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
