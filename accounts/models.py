from django.db import models

class Userreg(models.Model):
   
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    
    class Meta:
        db_table="userreg"

class Login(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    type   = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
     
    
    class Meta:
        db_table="login"



     
