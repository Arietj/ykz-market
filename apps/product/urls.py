from rest_framework.routers import DefaultRouter

from apps.product.views import CategoryViewSet, SubCategoryViewSet, ProductViewSet
from apps.orders.views import OrderItemViewSet, OrderViewSet
from apps.accounts.views import UserViewSet
from apps.cart.views import CartViewSet, CartItemViewSet

router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('sub-category', SubCategoryViewSet)
router.register('product', ProductViewSet)
router.register('order-item', OrderItemViewSet)
router.register('order', OrderViewSet)
router.register('user', UserViewSet)
router.register('cart', CartViewSet)
router.register('cart-item', CartItemViewSet)