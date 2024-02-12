from django.urls import path
from rest_framework import routers

from . import views
from .views import ShopView, CartView, ProductSingleView, CartViewSet, WishlistView

router = routers.DefaultRouter()
router.register(r'cart', CartViewSet)

app_name = 'store'

urlpatterns = [
    path('', ShopView.as_view(), name='shop'),
    path('cart/', CartView.as_view(), name='cart'),
    path('product/<int:id>/', ProductSingleView.as_view(), name='product'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('addproduct/<int:product_id>/', views.add_product, name='addproduct'),
    path('deleteproduct/<int:product_id>/', views.delete_product, name='deleteproduct')
]
