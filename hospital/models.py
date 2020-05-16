from django.db import models

# Create your models here.

class Hospitals(models.Model):
    id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=50)  # Field name made lowercase.
    city = models.CharField(max_length=50)  # Field name made lowercase.
    name = models.CharField(max_length=75)  # Field name made lowercase.
    category = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    medicine = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(max_length=300, blank=True, null=True)  # Field name made lowercase.
    website = models.CharField(max_length=100, blank=True, null=True)
    specilization = models.CharField(max_length=200, blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'hospitals'