from django.utils.translation import gettext_lazy as _
from django.db import models


class RSSPage(models.Model):

    html = models.TextField()
    url = models.URLField()
    website_name = models.TextField()
    collected_timestamp = models.DateTimeField(auto_now_add=True)