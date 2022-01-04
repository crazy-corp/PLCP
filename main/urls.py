from django.urls import path

from . import views
from .views import addbus

urlpatterns = [
    path('',views.index,name="index"),
    path("transmit",views.transmit),
    

]

# path('SFE/test',views.test,name="test"),
#     path('SFE/searchresult',views.searchresult,name="searchresult"),
#     path('SFE/addbus',addbus.as_view(),name="ADDBUS"),
#     path('SFE/scedule/<int:ID>',views.scedule,name="scedule"),
#     path('SFE/searchresult/scedule/<int:ID>',views.scedule,name="scedule2"),