from rest_framework import serializers
from models import houseinfo

class HouseinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = houseinfo

        fields = '__all__'