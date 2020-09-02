from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from upload.models import States, Cities

# Create your models here.

class Criminal(models.Model):
    criminal_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    phys_desc = models.CharField(blank=True, max_length=250)
    state = models.ForeignKey('upload.States', on_delete=models.CASCADE, default=11)
    city = ChainedForeignKey(
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
        return self.city.name + ', ' + self.state.name
