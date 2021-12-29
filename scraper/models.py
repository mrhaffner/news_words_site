from django.utils.translation import gettext_lazy as _
from django.db import models


class RSS_Page(models.Model):

    html = models.TextField()
    url = models.URLField()
    collected_timestamp = models.DateTimeField(auto_now_add=True)