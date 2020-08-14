from rest_framework import serializers
from api.models import Garden

class GardenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garden
        fields = ['id', 'gardenName']

    # id = serializers.IntegerField(read_only=True)
    # gardenName = serializers.CharField(required=False, allow_blank=True, max_length=100)

    # def create(self, validated_data):
    #     """
    #     Create and return a new Garden instance, given validated data
    #     """
    #     return Garden.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return and existing Garden instance, given validated data
    #     """
    #     instance.gardentName = validated_data.get('gardenName', instance.title)
    #     instance.save()
    #     return instance