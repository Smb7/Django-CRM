from django.contrib import admin
from .models import Record # adding our model for our db, this will show up in the admin page 

# Register your models here.
admin.site.register(Record)