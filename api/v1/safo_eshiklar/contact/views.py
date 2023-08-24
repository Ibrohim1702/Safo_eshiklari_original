from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from api.format.format import format_cnt
from api.v1.safo_eshiklar.contact.serializer import CntSerializer


class CntView(GenericAPIView):
    serializer_class = CntSerializer

    def post(self, requests, *args, **kwargs):
        data = requests.data
        ser = self.get_serializer(data=data)
        ser.is_valid(raise_exception = True)
        cnt = ser.save()

        return Response(format_cnt(cnt))

