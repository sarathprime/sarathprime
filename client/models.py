from django.db import models

class client(models.Model):
    yourname=models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    contact = models.CharField(max_length=150, null=True)


class client_purpose(models.Model):
    yourname=models.CharField(max_length=150)
    organisation = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    contact = models.CharField(max_length=150)
    purpose = models.CharField(max_length=150)
    booleann= models.BooleanField(default=False)


class money(models.Model):
    yourname=models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    buisness = models.CharField(max_length=150)
    employers= models.CharField(max_length=150)
    targetamount = models.CharField(max_length=150)
    file = models.FileField(upload_to='files')


class link_amount(models.Model):
    name=models.CharField(max_length=150)
    ifsc = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    state = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    dob = models.CharField(max_length=150)
    number = models.CharField(max_length=150)
    type = models.CharField(max_length=150)
    cash = models.CharField(max_length=150)
    targetamount1 = models.CharField(null=True,max_length=150)
