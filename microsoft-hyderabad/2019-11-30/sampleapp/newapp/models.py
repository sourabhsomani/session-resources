from django.db import models

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=100, blank=False)
    Email = models.CharField(max_length=100, blank=False)
    Contact_Number=models.CharField(max_length=15, blank=True)

    def __str__(self):
        return "{0} {1} {2}".format(
            self.Name,
            self.Email,
            self.Contact_Number
        )