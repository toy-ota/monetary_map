from django.contrib import admin
from .models import ItemModel, StoreItemRelation, StoreModel, PurchaseModel, PurchaseDetailModel

# Register your models here.

admin.site.register(ItemModel)
admin.site.register(StoreModel)
admin.site.register(StoreItemRelation)
admin.site.register(PurchaseModel)
admin.site.register(PurchaseDetailModel)