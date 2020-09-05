from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30, primary_key=True)
    phone = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    message = models.TextField()
    contact = models.ForeignKey('Contact', on_delete=models.CASCADE)

    def __str__(self):
        return self.contact.name
