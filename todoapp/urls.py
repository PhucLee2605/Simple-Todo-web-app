from django.urls import path
from django.urls.conf import include
from rest_framework import routers

from .views import  todoListViewClass, remove


# router = routers.SimpleRouter()
# router.register()

urlpatterns = [
    path('',todoListViewClass.as_view(),name = 'home'),
    path('del/<int:item_id>',remove,name ='delete')
]
