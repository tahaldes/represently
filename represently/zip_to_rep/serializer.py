from .models import Zipcode, Rep

from rest_framework import serializers

class RepInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rep
        fields = '__all__'

class ZipRepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zipcode
        fields = 'zip'