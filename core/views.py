from rest_framework import generics

from .models import Catalogo, Area, Item
from .serializers import CatalogoSerializer, AreaSerializer, Item

class CatalogoList(generics.ListCreateAPIView):
    """
    Lista y crear Catalogos
    """
    queryset = Catalogo.objects.all()
    serializer_class = CatalogoSerializer


class CatalogoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Ver, Editar y Eliminar Catalogos
    """
    queryset = Catalogo.objects.all()
    serializer_class = CatalogoSerializer


class AreaList(generics.ListCreateAPIView):
    """
    Lista y crear Areas
    """
    serializer_class = AreaSerializer

    def get_queryset(self):
        queryset = Area.objects.all()
        catalogo_id = self.request.query_params.get('catalogo', None)
        if catalogo_id is not None:
            queryset = queryset.filter(catalogo__id=catalogo_id)
        return queryset


class AreaDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Ver, Editar y Eliminar Areas
    """
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class ItemList(generics.ListCreateAPIView):
    """
    Lista y crear Items
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        area_id = self.request.query_params.get('area', None)
        if area_id is not None:
            queryset = queryset.filter(area__id=area_id)
        return queryset


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Ver, Editar y Eliminar Items
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer