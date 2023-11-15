from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120,null=True, blank=True)
    email = models.EmailField(max_length=80,null=True, blank=True)
    phone = models.CharField(max_length=120,null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.first_name)