from django.db import models

# Create your models here.
class Criminal(models.Model):
    criminal_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    phys_desc = models.CharField(blank=True, max_length=250)
    location = models.CharField(max_length=2)
    photo = models.ImageField(blank=True, upload_to='criminals/', default='criminals/missing.jpeg')
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.name