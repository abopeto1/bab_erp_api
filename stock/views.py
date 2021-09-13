from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from stock.models import Item, Warehouse
from stock.serializers import ItemSerializer, WarehouseSerializer


@api_view(['GET', 'POST'])
def item_list(request, format=None):
    """
    List all items, or create a new one
    :param format:
    :param request:
    :return:
    """
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WarehouseList(generics.ListCreateAPIView):
    """
    List all warehouses, or create a new one
    """
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class WarehouseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
