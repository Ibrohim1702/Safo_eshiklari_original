from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from Safo_eshiklari.models import Basket, Products
from api.format.format import basketFormat


class BasketView(GenericAPIView):

    def post(self, requests, *args, **kwargs):
        data = requests.data

        if "prod_id" not in data:
            return Response({
                "Error": "Prod id berilmagan"
            })

        prod = Products.objects.filter(pk=data['prod_id']).first()

        if prod:
            baskett = Basket.objects.get_or_create(
                product=prod,
            )[0]


            baskett.quantity = data.get('quantity', baskett.quantity)
            baskett.save()

            return Response({
                "result": basketFormat(baskett)
            })

        else:
            return Response({
                "Error": "Noto'gri prod berilgan"
            })