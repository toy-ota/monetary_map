from django.shortcuts import render
from django.views.generic.list import ListView
from .models import PurchaseDetailModel, PurchaseModel
from django.db.models import Sum
from django.http import JsonResponse
from django.core import serializers
from django.db.models import F
# import json


def storeitemfunc(request):
    data = PurchaseModel.objects.prefetch_related(
        ).all(
        ).annotate(
            # total_price=Sum('purchasedetailpurchase__price__price'),
            total_price=Sum(F('purchasedetailpurchase__price__price') * F('purchasedetailpurchase__number_of_item'))
        )
    # purchase_data = PurchaseDetailModel.objects.all()
    params = {
        'data': data,
        # 'purchase_data': purchase_data
    }
    print(params)
    return render(request, 'index.html', params)


def ajax_number(request):
    queryID = int(request.POST.get('superID'))

    storeData = PurchaseModel.objects.prefetch_related(
        ).all(
        ).filter(pk=queryID).annotate(
            total_price=Sum(F('purchasedetailpurchase__price__price') * F('purchasedetailpurchase__number_of_item'))
        )
    store_list = [
        [storeObject.store.store, 
        int(storeObject.total_price * (1+storeObject.tax)), 
        int(storeObject.total_price * storeObject.tax),
        storeObject.purchase_time
        ]
        for storeObject in storeData
    ]

    purchase_list = [
        [ingredient.item.title, ingredient.price.price, ingredient.number_of_item, int(ingredient.price.price*ingredient.number_of_item)]
        for ingredient in PurchaseDetailModel.objects.all().filter(purchase=queryID)
    ]

    params = {
        'store_list': store_list,
        'purchase_list': purchase_list,
    }
    print(params)
    return JsonResponse(params)