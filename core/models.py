from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    '''
        Redefine user instances for the application
    '''
    email = models.EmailField(unique=True)
    # vendor = models.BooleanField('Vendor', default=False)
    # merchant = models.BooleanField('Merchant', default=False)



class VendorProfile(models.Model):
    '''
        Class that handles enterprise/partner restaurants profile
    '''
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT
    )
    company_name = models.CharField(max_length=255)
    company_email = models.EmailField()
    location = models.CharField(max_length=255)
    company_description = models.TextField()
    owner = models.BooleanField(default=True)


class MerchantProfile(models.Model):
    '''
        Class that handles third-party collaborators
        i.e delivery associates
    '''
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT
    )
    merchant_name = models.CharField(max_length=255)
    merchant_email_address = models.EmailField()
    merchant_descrption= models.TextField()
