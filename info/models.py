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

class Publication(models.Model):
    title = models.CharField(_('title'), max_length=200, blank=False)
    author = models.TextField(_('author'), blank=False)
    prime_author = models.ForeignKey(
        TeamMember,
        on_delete=models.CASCADE,
    )
    publisher = models.CharField(_('journal'), max_length=200, null=True)
    year = models.IntegerField(_('year'), blank=False)
    arxiv_url = models.URLField('arxiv', null=True)
    ads_url = models.URLField('ADS', null=True)
    pdf_file = models.FileField(
        _('PDF file'), 
        upload_to='publications/', 
        null=True,
    )

    def __str__(self):
        return f"{self.prime_author} {self.year}"

