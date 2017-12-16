from rest_framework import serializers

from .models import Catalogo, Area, Item

class CatalogoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Catalogo
        fields = '__all__'


class AreaSerializer(serializers.ModelSerializer):
    catalogo = CatalogoSerializer(many=False, required=True)
    
    class Meta:
        model = Area
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    area = AreaSerializer(many=False, required=True)
    
    class Meta:
        model = Item
        fields = '__all__'