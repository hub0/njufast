from django.db import models
from core.models import User
from PIL import Image
from django.utils.translation import gettext_lazy as _

class Affiliation(models.Model):
    name = models.CharField(_('affiliation name'), max_length=200, 
        unique=True, blank=False)
    abbreviation = models.CharField(_('abbreviation'), max_length=20, 
        unique=True, blank=True)
    address = models.TextField(_('address'), blank=True)
    logo = models.ImageField(_('logo'), default='default.jpg', 
        upload_to='affiliation_logos')

    def __str__(self):
        return self.name

class TeamMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    affiliation = models.ForeignKey(
        Affiliation,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.user.name

