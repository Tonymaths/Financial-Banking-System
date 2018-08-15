from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=130, blank=False)
    email = models.EmailField(blank=False, null=True, max_length=130)
    message = models.CharField(max_length=830)

    def __str__(self):
        return self.name
