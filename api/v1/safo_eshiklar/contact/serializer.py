from rest_framework import serializers

from Safo_eshiklari.models import Contact


class CntSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'