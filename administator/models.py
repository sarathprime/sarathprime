from django.db import models

class currency(models.Model):
    administrator=models.CharField(max_length=150)
    currency = models.CharField(max_length=150)
    purpose = models.CharField(max_length=150)
    what=models.CharField(max_length=150)
    license = models.CharField(max_length=150)
    value = models.CharField(max_length=150)


class value_set(models.Model):
    administrator=models.CharField(max_length=150)
    currency = models.CharField(max_length=150)
    purpose = models.CharField(max_length=150)
    what=models.CharField(max_length=150)
    license = models.CharField(max_length=150)
    value = models.CharField(max_length=150)


class r_w(models.Model):
    email=models.EmailField(max_length=150)
    generate_id = models.IntegerField()


class donor_id_generate(models.Model):
    email=models.EmailField(max_length=150)
    id_donor = models.CharField(max_length=150)

