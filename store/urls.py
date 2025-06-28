from django.urls import path
from .views import RegisterView
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('categories', CategoryViewSet, basename='categories')
router.register('cart', CartViewSet, basename='cart')
router.register("order", OrderViewSet, basename='order')
router.register("admin/orders", AdminOrderViewSet, basename='admin-orders')








urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('place-order/', PlaceOrderView.as_view(), name='place-order'),
]

urlpatterns += router.urls
