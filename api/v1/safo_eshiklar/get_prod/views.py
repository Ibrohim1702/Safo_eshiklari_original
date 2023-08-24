from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from Safo_eshiklari.models import Products
from api.format.format import productFormat
from api.v1.safo_eshiklar.get_prod.serializer import ProductSerializer


class ProductView(GenericAPIView):
    serializer_class = ProductSerializer

    def get(self, *args, **kwargs):
        prod = Products.objects.all()
        l = []
        for i in prod:
            l.append(productFormat(i))

        return Response({
            "result": l
        })
