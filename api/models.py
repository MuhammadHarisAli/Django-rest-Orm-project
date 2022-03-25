from django.db import models
from django.utils.translation import gettext_lazy as _

class DataSetModel(models.Model):
    date = models.DateTimeField(
        verbose_name=_('Creation date'),
    )
    channel = models.CharField(
        max_length=200,
    )
    country = models.CharField(
        max_length=200,
    )
    os = models.CharField(
        max_length=200,
    )
    impressions = models.SmallIntegerField(
    )
    clicks = models.SmallIntegerField(
    )
    installs = models.SmallIntegerField(
    )
    spend = models.FloatField(
    )
    revenue = models.FloatField(
    )