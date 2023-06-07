from django.db import models

class technical(models.Model):
    yourname=models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    contact = models.CharField(max_length=150, null=True)





class wallet_entry(models.Model):
    teamname=models.EmailField(max_length=150)
    purpose = models.CharField(max_length=150)
    bt = models.BooleanField(default=False)