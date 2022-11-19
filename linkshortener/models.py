from django.db import models



class Shortener(models.Model):
    url = models.CharField(max_length=255, db_index=True, unique=True)
    shortener = models.CharField(max_length=255, db_index=True)
    clicks = models.IntegerField(default=0)


    def clicks_increament(self):
        self.clicks += 1 
        self.save()

        

