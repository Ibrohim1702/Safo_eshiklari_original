from django.urls import path

from api.v1.safo_eshiklar.basket.views import  BasketView
from api.v1.safo_eshiklar.contact.views import CntView
from api.v1.safo_eshiklar.get_prod.views import ProductView
from api.v1.safo_eshiklar.get_prod_id.views import Prod_get

urlpatterns = [
    path("get_prod_id/<int:pk>/", Prod_get.as_view()),
    path("get_prod/", ProductView.as_view()),
    path("basket/<int:pk>/", BasketView.as_view()),
    path("cnt/", CntView.as_view()),
]