from django.db import models

from accounting.models import Company
from utils.models import EntityCommonInfo


# A Warehouse in `BAB_ERP` is a storage location for your products
# User must create that before create any items
class Warehouse(EntityCommonInfo):
    is_group = models.BooleanField()
    parent = models.ForeignKey('Warehouse', on_delete=models.CASCADE, verbose_name="parent warehouse", null=True)
    company = models.ForeignKey('accounting.Company', on_delete=models.CASCADE, verbose_name="company of warehouse")
    owner = models.ForeignKey('users.User', related_name='warehouses', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class UoM(EntityCommonInfo):
    abbreviation = models.CharField(max_length=10, blank=False, null=False)

    class Meta:
        ordering = ['created']


class ItemGroup(EntityCommonInfo):
    class Meta:
        ordering = ['created']


class Item(EntityCommonInfo):
    item_group = models.ForeignKey(ItemGroup, on_delete=models.CASCADE)
    code = models.CharField(max_length=100, blank=True, null=True)
    open_stock = models.IntegerField(default=0, blank=False, null=False)
    is_stock = models.BooleanField(default=False)
    default_uom = models.ForeignKey(UoM, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    description = models.TextField()
    # brand = models.ForeignKey

    class Meta:
        ordering = ['created']
