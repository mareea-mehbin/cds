from django.db import models
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.

class States(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Cities(models.Model):
    name = models.CharField(max_length=30)
    state = models.ForeignKey('States', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Criminal(models.Model):
    criminal_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    phys_desc = models.CharField(blank=True, max_length=250)
    state = models.ForeignKey('States', on_delete=models.CASCADE, default=11)
    #city = models.ForeignKey('Cities', on_delete=models.CASCADE, default=709)
    country = ChainedForeignKey(
        Cities,
        chained_field="state",
        chained_model_field="state",
        show_all=False,
        auto_choose=True,
        sort=True)
    photo = models.ImageField(blank=True, upload_to='criminals/', default='criminals/missing.jpeg')
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.name
    
    def location(self):
        return self.city + ', ' + self.state
