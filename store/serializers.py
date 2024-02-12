from rest_framework import serializers
from .models import Cart, Wish


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class WishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wish
        fields = '__all__'