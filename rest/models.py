from django.db import models

class Menu(models.Model):
    types=models.CharField(max_length=50)
    image= models.ImageField(upload_to='image_res',blank=True, null=True)


    def __str__(self):
     return self.types

class Plate(models.Model):
   name=models.CharField(max_length=50, default='')
   typ = models.ForeignKey(Menu,related_name='rest', on_delete= models.CASCADE)
   ing = models.TextField(blank=True, null=True)
   image= models.ImageField(upload_to='image_res',blank=True, null=True)
   prix= models.FloatField()

   def __str__(self):
      return f"{self.name} {self.typ} "

