from rest_framework import serializers
from .models import Product, ProductInventory


class InventoryCountField(serializers.RelatedField):
    def to_representation(self, value):
        if value:
            return value.inventory_count
        return None


class ProductSerializer(serializers.ModelSerializer):
    inventory_count = InventoryCountField(
        source='productinventory_set.first', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'inventory_count']
