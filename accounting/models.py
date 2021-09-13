from django.db import models
from utils.choices_list import CURRENCY_AVAILABLE, COUNTRY_CHOICES


class Company(models.Model):
    """
    A Company is a legal entity having a R.C.C.M
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True)
    owner = models.ForeignKey('users.User', related_name='companies', on_delete=models.CASCADE)

    # Basic Infos
    name = models.CharField(max_length=200, blank=False, null=False)
    abbr = models.CharField(max_length=10, blank=False, null=False)
    establishment_date = models.DateField(null=True)

    # Settings
    default_currency = models.CharField(choices=CURRENCY_AVAILABLE, max_length=4, blank=False, default="USD")
    # domain = domain of company. e.g: manufacturing, services

    # parent_company = if has parent company
    tax_id = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField()

    # Extra Infos
    country = models.CharField(choices=COUNTRY_CHOICES, max_length=2, null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    # fax
    email = models.CharField(max_length=30, null=True, blank=True)
    # website
    # address
    # logo = Image FK

    class Meta:
        ordering = ['created']
