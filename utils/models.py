from django.db import models


class EntityCommonInfo(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
