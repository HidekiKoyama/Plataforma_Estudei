from django.db import models

class categorie_curses(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(max_length=150)
    active = models.BooleanField(default=True, blank=False)