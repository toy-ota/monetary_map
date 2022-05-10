"""priceplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from debug_toolbar import APP_NAME
from django.urls import path, include
from .views import storeitemfunc, ajax_number

app_name = 'item'

urlpatterns = [
    path('', storeitemfunc, name='map'),
    path('ajax-number/', ajax_number, name='ajax_number'),
    # path('store/', ItemList.as_view()),
]