from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import InvoiceSerializer
from product.models import Invoice, Product


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all().order_by('created')
    serializer_class = InvoiceSerializer
    permission_classes = (IsAuthenticated, )
