from django.db import models

# Create your models here.

class Customer(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)


	def __str__(self):
		return self.email
class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)
	

	def __str__(self):
		return self.name

class Products(models.Model):
    CATEGORY = (
        ('indoor', 'Indoor'),
        ('outdoor', 'Outdoor'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name






class Order(models.Model):
    STATUS = (
        ('pending', 'pending'),
        ('out of delivery', 'out of delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Products, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    tag= models.ManyToManyField(Tag)

    def __str__(self):
        return self.product.name



class Emp(models.Model):
    Salary = (
        ('pending', 'pending'),
        ('Provide', 'provide'),
    )  
    name = models.CharField(max_length=200, null=True)
    number = models.CharField(max_length=50, null=True) 
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    Month = models.CharField(max_length=200, null=True, choices=Salary)

    def __str__(self):
        return self.name
