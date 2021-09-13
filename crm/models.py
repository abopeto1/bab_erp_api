from django.db import models

from utils.choices_list import COUNTRY_CHOICES
from utils.models import EntityCommonInfo


class Customer(EntityCommonInfo):
    class Meta:
        ordering = ['created']


class Address(models.Model):
    # address_type =
    address_title = models.CharField(max_length=100, blank=False, null=False)
    address_line1 = models.CharField(max_length=100, blank=False, null=False)
    address_line2 = models.CharField(max_length=100, blank=True, null=True)
    city_or_town = models.CharField(max_length=100, blank=False, null=False)
    county = models.CharField(max_length=100, blank=True, null=True)
    state_or_province = models.CharField(max_length=100, blank=False, null=False)
    country = models.CharField(choices=COUNTRY_CHOICES, default='DRC')
    email = models.EmailField()
    phone_1 = models.CharField(max_length=14, blank=True, null=True)
    phone_2 = models.CharField(max_length=14, blank=True, null=True)
    fax = models.CharField(max_length=14, blank=True, null=True)
