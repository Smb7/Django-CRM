from django.db import models

# django code no sql code 
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) # this will slap a time stamp
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50) 
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=20)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
    



