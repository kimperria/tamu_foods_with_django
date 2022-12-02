from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField

class User(AbstractUser):
    '''
        Redefine user instances for the application
    '''
    email = models.EmailField(unique=True)
    profile_photo = CloudinaryField('images/',default='https://res.cloudinary.com/dbgbail9r/image/upload/v1669642977/tamu_foods_with_django/user_profile_image_n5g3kg.png')
    is_customer = models.BooleanField('Is customer', default=False)
    is_vendor = models.BooleanField('Is vendor', default=False)
    is_merchant = models.BooleanField('Is merchant', default=False)




class Vendor(models.Model):
    '''
        Class that handles enterprise/partner restaurants profile
    '''
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT
    )
    PENDING_APPROVAL_BY_ADMIN = 'P'
    APPROVED_BY_ADMIN = 'A'
    REJECTED_BY_ADMIN = 'R'
    APPROVAL_CHOICES = [
        (PENDING_APPROVAL_BY_ADMIN, 'pending' ),
        (APPROVED_BY_ADMIN, 'approved' ),
        (REJECTED_BY_ADMIN, 'rejected' )
    ]
    approval_status = models.CharField(
        max_length=1,
        choices=APPROVAL_CHOICES,
        default=PENDING_APPROVAL_BY_ADMIN
    )
    company_name = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    company_description = models.TextField(blank=True)
    # owner = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


class Merchant(models.Model):
    '''
        Class that handles third-party collaborators
        i.e delivery associates
    '''
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT
    )
    PENDING_APPROVAL_BY_ADMIN = 'P'
    APPROVED_BY_ADMIN = 'A'
    REJECTED_BY_ADMIN = 'R'
    APPROVAL_CHOICES = [
        (PENDING_APPROVAL_BY_ADMIN, 'pending' ),
        (APPROVED_BY_ADMIN, 'approved' ),
        (REJECTED_BY_ADMIN, 'rejected' )
    ]
    approval_status = models.CharField(
        max_length=1,
        choices=APPROVAL_CHOICES,
        default=PENDING_APPROVAL_BY_ADMIN
    )
    merchant_name = models.CharField(max_length=255)
    merchant_description= models.TextField()

    def __str__(self):
        return self.user.username
