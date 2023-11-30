from django.db import models
from django.db.models import CASCADE


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_created=True, auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True, auto_created=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Employee(BaseModel):
    id = models.AutoField(primary_key=True, editable=False)
    full_name = models.CharField()
    birthdate = models.DateField()

    def __str__(self):
        return self.full_name


class Client(BaseModel):
    id = models.AutoField(primary_key=True, editable=False)
    full_name = models.CharField()
    birthdate = models.DateField()

    def __str__(self):
        return self.full_name


class Order(BaseModel):
    id = models.AutoField(primary_key=True, editable=False)
    price = models.FloatField()
    date = models.DateTimeField()
    employee = models.ForeignKey(Employee, related_name='orders', on_delete=CASCADE)
    client = models.ForeignKey(Client, related_name='orders', on_delete=CASCADE)


class Product(BaseModel):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField()
    quantity = models.IntegerField()
    price = models.FloatField()
    order = models.ForeignKey(Order, related_name='products', on_delete=CASCADE)

    def __str__(self):
        return self.name
