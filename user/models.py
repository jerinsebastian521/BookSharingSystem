from django.db import models
from django.db import connections
# Create your models here.

class Books(models.Model):
   
    bid = models.AutoField(primary_key=True)
    bookname = models.CharField(max_length=100)
    bookauthor = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/image/ % Y/% m/% d/')
    sr = models.CharField(max_length=100)
    userid = models.CharField(max_length=100)

    class Meta:
        db_table="books"
