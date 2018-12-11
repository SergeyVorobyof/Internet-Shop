from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=200)
    type_of_product = models.CharField(max_length=200)
    date_of_manufacture = models.DateTimeField(blank=True, null=True)
    warranty = models.IntegerField(default = 1)


class Courier(models.Model):
    name = models.CharField(max_length=200)
    date_of_hire = models.DateTimeField(default = timezone.now)
    working_days = models.TextField()
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)

#Full fields
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)

    def register(self):
        self.save()

    def __str__(self):
        return self.name


class Order(models.Model):
    #order_id = models.AutoField(primary_key=True)
    cust_id = models.ForeignKey(Customer, on_delete = models.CASCADE, related_name = 'orders')
    form_of_payment = models.CharField(max_length=200)
    address = models.TextField()
    date_completed = models.DateTimeField()
    delivery_type = models.CharField(max_length=200)
    notes = models.TextField()


class Good(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    holder = models.ForeignKey(Order, on_delete = models.CASCADE, related_name = 'goods', default = None)
    #picture = models.ImageField(upload_to='good_detail/<int:pk>'))

class Bucket(models.Model):
    order = models.ForeignKey(Order, on_delete = models.CASCADE, related_name = 'bucket')

class Storage(models.Model):
    ident_num = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=200)
    num_of_products = models.IntegerField(default=1)
    name_of_product = models.CharField(max_length=200)
    date = models.DateTimeField()

class Material(models.Model):
    num_of_products = models.IntegerField(default=1)
    name_of_product = models.CharField(max_length=200)



