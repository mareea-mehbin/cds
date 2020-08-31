from django.contrib import admin
from .models import Contact, ContactMessage

# Register your models here.
admin.site.register(Contact)
admin.site.register(ContactMessage)