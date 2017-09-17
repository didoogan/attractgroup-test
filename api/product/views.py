from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.product.serializers import ProductSerializer
from product.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-name')
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated)
