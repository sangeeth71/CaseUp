from django.db import models

# Create your models here.
class CategoryDb(models.Model):
    Material_Name=models.CharField(max_length=50,null=True,blank=True)
    Description=models.CharField(max_length=200,null=True,blank=True)
    Image=models.ImageField(upload_to="material_image",null=True,blank=True)
class CaseDb(models.Model):
    Cover_Name=models.CharField(max_length=100,null=True,blank=True)
    Phone_Model=models.CharField(max_length=100,null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Material=models.CharField(max_length=100,null=True,blank=True)
    Description=models.CharField(max_length=200,null=True,blank=True)
    Cover_Image=models.ImageField(upload_to="cover image",null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)