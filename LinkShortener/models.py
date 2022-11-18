from django.db import models



class Shortener(models.Model):
    url = models.CharField(max_length=500, db_index=True)
    shortener = models.CharField(max_length=255, db_index=True)


