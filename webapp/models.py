from django.db import models

# Create your models here.
class RegistrationDb(models.Model):
    User_Name=models.CharField(max_length=100,null=True,blank=True)
    Password=models.CharField(max_length=100,null=True,blank=True)
    Confirm_Password=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
class MessageDb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100, null=True, blank=True)
    Message=models.CharField(max_length=600,null=True,blank=True)
class CartDB(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    CoverName = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Total_Price = models.IntegerField(null=True, blank=True)
    Case_Image = models.ImageField(upload_to="Cart_Images", null=True, blank=True)

    def __str__(self):
        return self.CoverName
class OrderDb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Address=models.CharField(max_length=200,null=True,blank=True)
    Appartment=models.CharField(max_length=100,null=True,blank=True)
    City=models.CharField(max_length=100,null=True,blank=True)
    Postcode=models.IntegerField(null=True,blank=True)
    Phone=models.IntegerField(null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.Name