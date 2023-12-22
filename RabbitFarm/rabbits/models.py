# rabbits/models.py
from django.db import models
from django.utils.translation import gettext_lazy as _

class Rabbit(models.Model):
    GENDER_CHOICES = [
        ('M', _('Male')),
        ('F', _('Female')),
    ]

    name = models.CharField(_("Name"), max_length=100)
    age = models.PositiveIntegerField(_("Age"))
    gender = models.CharField(_("Gender"), max_length=1, choices=GENDER_CHOICES)
    color = models.CharField(_("Color"), max_length=50)
    weight = models.FloatField(_("Weight"))
    birth_date = models.DateField(_("Birth Date"))
    date_acquired = models.DateField(_("Date Acquired"))
    notes = models.TextField(_("Notes"), blank=True, null=True)
    image = models.ImageField(upload_to='rabbit_images/', null=True, blank=True)
    class Meta:
        verbose_name = _("Rabbit")
        verbose_name_plural = _("Rabbits")

    def __str__(self):
        return self.name
