from django.db import models

class categorie_curses(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(max_length=150)
    active = models.BooleanField(default=True, blank=False)

    def __str__(self):
        return self.name
    
    
class courses(models.Model):
    user_log = models.ForeignKey("auth.user", blank=True, null=True ,on_delete=models.SET_NULL, default="")
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=155)
    categorie_couse = models.IntegerField(null=False, blank=True, default="")
    
    def __str__(self):
        return self.name