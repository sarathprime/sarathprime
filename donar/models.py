from django.db import models

class donor(models.Model):
    yourname=models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    contact = models.CharField(max_length=150, null=True)


class donor_purpose(models.Model):
    yourname=models.CharField(max_length=150)
    organisation = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    contact = models.CharField(max_length=150)
    purpose = models.CharField(max_length=150)
    b3= models.BooleanField(default=False)


class tax_amount(models.Model):
    amount=models.CharField(max_length=150)


class reciptient_amount(models.Model):
    amount=models.CharField(max_length=500)
    recipitent=models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    update = models.BooleanField(default=False)
    ecrypt= models.CharField(max_length=500, null=True)
    b5=models.BooleanField(default=False)


class donor_link_amount(models.Model):
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
    update = models.BooleanField(default=False)