from rest_framework.generics import GenericAPIView

from Safo_eshiklari.models import Products
from rest_framework.response import Response

from api.format.format import prod_res, productFormat


class Prod_get(GenericAPIView):
    def get(self, requests, pk=None, *args, **kwargs):
        prod_id = Products.objects.filter(id=pk).first()

        if not prod_id:
            return Response({"Error": "Bunaqa id li product topilmadi"})

        return Response(productFormat(prod_id))

