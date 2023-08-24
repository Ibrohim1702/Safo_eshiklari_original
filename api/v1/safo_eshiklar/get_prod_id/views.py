from rest_framework.generics import GenericAPIView

from Safo_eshiklari.models import Products
from rest_framework.response import Response

from api.format.format import prod_res


class Prod_get(GenericAPIView):

    def get(self, pk=None, *args, **kwargs):
        prod = Products.objects.filter(pk=pk).first()
        l = []
        for i in prod:
            l.append(prod_res(i))

        root = Products.objects.filter(product=prod)
        l = []
        for i in root:
            l.append(prod_res(i))