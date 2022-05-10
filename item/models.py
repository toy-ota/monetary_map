from re import I
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ItemModel(models.Model):
    title = models.CharField(max_length=100)
    kind = models.CharField(max_length=100)
    reputation = models.TextField(
        verbose_name='',
        blank=True,
        null=True,
        max_length=1000,
    )

    def __str__(self):
        return f"{self.kind}/{self.title}"


class StoreModel(models.Model):
    store = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    storeimage = models.ImageField(upload_to='', blank=True, null=True)
    # goods = models.ManyToManyField(ItemModel, through="StoreItemRelation")

    def __str__(self):
        return f"{self.store}"


class StoreItemRelation(models.Model):
    store = models.ForeignKey("StoreModel", on_delete=models.CASCADE)
    item = models.ForeignKey("ItemModel", on_delete=models.CASCADE)
    joined_date = models.DateTimeField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.store}-{self.item}"


class PurchaseModel(models.Model):
    purchase_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey("StoreModel", on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=100, default='cash')
    tax = models.FloatField(default='0.1')
        
    def __str__(self):
        return f"{self.purchase_time}-{self.store}"
    

class PurchaseDetailModel(models.Model):
    purchase = models.ForeignKey("PurchaseModel", on_delete=models.CASCADE, related_name="purchasedetailpurchase")
    item = models.ForeignKey("ItemModel", on_delete=models.CASCADE)
    price = models.ForeignKey("StoreItemRelation", on_delete=models.CASCADE)
    number_of_item = models.IntegerField(default='1')

    def __str__(self):
        return f"{self.purchase}-{self.item}"