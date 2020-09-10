from django.contrib import admin
from .models import Criminal, States, Cities

# Register your models here.
admin.site.register(Criminal)
admin.site.register(States)
admin.site.register(Cities)