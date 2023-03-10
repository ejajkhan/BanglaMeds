from django.db import models

class Medtype(models.Model):
    name=models.CharField(max_length=30,null=True,blank=True)
    description = models.CharField(max_length=1000, null=True,blank=True)

    def __str__(self):
        return self.name


class Disease(models.Model):
    name=models.CharField(max_length=30,null=True,blank=True)
    description=models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self):
        return self.name

class Medicine(models.Model):
    name=models.CharField(max_length=30,default="")
    description=models.CharField(max_length=1000,default="")
    type=models.ForeignKey(Medtype,on_delete=models.SET_DEFAULT,default="We will update soon")
    company=models.CharField(max_length=30,null=True,blank=True)
    disease=models.ForeignKey(Disease,on_delete=models.SET_DEFAULT,default="We will update soon")
    image = models.ImageField(upload_to='shop/images', null=True,blank=True)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)

    def available(self):
        if self.quantity:
            return "Available "+str(self.quantity)+" pieces"
        else:
            return "Not Available"

    def __str__(self):
        return self.name
