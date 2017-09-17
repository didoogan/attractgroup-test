from rest_framework import routers

from .invoice.views import InvoiceViewSet
from .product.views import ProductViewSet

router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('invoices', InvoiceViewSet)

urlpatterns = []

urlpatterns += router.urls
