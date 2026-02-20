from rest_framework.routers import DefaultRouter


from product.views import CategoryViewSet, SubCategoryViewSet, ProductViewSet, OrderItemViewSet, OrderViewSet

router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('sub-category', SubCategoryViewSet)
router.register('product', ProductViewSet)
router.register('order-item', OrderItemViewSet)
router.register('order', OrderViewSet)