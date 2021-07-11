import datetime

from django.conf import settings
from django.contrib.gis.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class ServiceProvider(models.Model):

    name = models.CharField(verbose_name=_("Service Provider Name"), max_length=150)

    email = models.EmailField(_("Service Provider Email"), max_length=150)
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17)
    language = models.CharField(max_length=50, default=settings.LANGUAGE_CODE)
    currency = models.CharField(max_length=50, default="USD")
    created_at = models.DateTimeField(default=timezone.now, blank=False, editable=False)
    updated_at = models.DateTimeField(blank=False, editable=True, auto_now=True)

    def __str__(self):
        return self.name


class ServiceArea(models.Model):

    service_provider = models.ForeignKey(
        ServiceProvider,
        on_delete=models.CASCADE,
        related_name="provider",
    )

    name = models.CharField(verbose_name=_("Service Area Name"), max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    service_area = models.PolygonField()
    created_at = models.DateTimeField(default=timezone.now, blank=False, editable=False)
    updated_at = models.DateTimeField(blank=False, editable=True, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
