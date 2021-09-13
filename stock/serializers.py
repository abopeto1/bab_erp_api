from rest_framework import serializers

from stock.models import Item, Warehouse


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name']


class WarehouseSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.HyperlinkedRelatedField(view_name='user', )

    class Meta:
        model = Warehouse
        fields = ['id', 'name', ]
