from django.db import models
from django.db.models.fields import CharField
from django.utils import timezone

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=300)
    password = models.CharField(max_length=300)

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def __str__(self):
        return "Username: " + self.username + ", Password" + self.password

class Food(models.Model):
    name = models.CharField(max_length=300)
    desc = models.CharField(max_length=300)
    price = models.FloatField(max_length=300)
    created_at = models.DateTimeField(blank=True, null=True)

    def getName(self):
        return self.name

    def getDesc(self):
        return self.desc

    def getPrice(self):
        return self.price

    def __str__(self):
        return str(self.pk) + ': '  + self.name + ' - ' + str(self.price) + ', ' + self.desc + ' created at: ' + str(self.created_at)

class Customer(models.Model):
    name = CharField(max_length=300)
    address = CharField(max_length=300)
    city = CharField(max_length=300)

    def getName(self):
        return self.name
    
    def getAddress(self):
        return self.address

    def getCity(self):
        return self.city

    def __str__(self):
        return str(self.pk) + ": " + self.name + ' - ' + self.address + ', ' + self.city

class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    qty = models.FloatField(max_length=300)
    ordered_at = models.DateTimeField(blank=True, null=True)
    cust_order = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment_mode = models.CharField(max_length=300)

    def getMode(self):
        return self.payment_mode

    def getQuantity(self):
        return self.qty

    def __str__(self):
        return str(self.pk) +": " + str(self.food) + " (" + str(self.qty) + "). For " + str(self.cust_order) + self.payment_mode + "ordered at " + str(self.ordered_at)
