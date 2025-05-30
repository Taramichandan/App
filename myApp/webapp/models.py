from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return (f"{self.first_name} {self.email} {self.phone} {self.address} {self.city} {self.state} {self.zip_code} {self.created_at}")

# Create your models here.
