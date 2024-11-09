from django.db import models


# Create your models here.


class RealEstate(models.Model):

    address=models.CharField(max_length=100)

    price=models.PositiveIntegerField()

    property_type=models.CharField(max_length=20)

    number_of_bedrooms=models.PositiveBigIntegerField()

    square_footage=models.PositiveBigIntegerField()

    location=models.CharField(max_length=100)

    property_image=models.ImageField(upload_to="realestateimg",null=True)


    contact_detaild=models.CharField(max_length=100)



    def __str__(self):      

     return self.address