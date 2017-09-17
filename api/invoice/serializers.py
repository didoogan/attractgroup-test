from api.product.serializers import ProductSerializer
from django.contrib.auth import get_user_model
from product.models import Invoice
from rest_framework import serializers

from api.user.serializers import UserSerializer

from product.models import Product


class InvoiceSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    products = ProductSerializer(many=True, read_only=True)
    total = serializers.FloatField(read_only=True)

    class Meta:
        model = Invoice
        fields = ('id', 'user', 'products', 'created', 'closed', 'total', )

    def create(self, validated_data):
        user_id = self.context.get('request').data.get('user')
        product_id = self.context.get('request').data.get('product')
        User = get_user_model()
        user = User.objects.get(id=user_id)
        inctance = Invoice(user=user)
        inctance.save()
        inctance.products.add(product_id)
        return inctance

    def update(self, instance, validated_data):
        product_id = self.context['request'].data.get('product_id', False)
        status = self.context['request'].data.get('status', None)
        if product_id and int(product_id) not in \
                instance.products.all().values_list('id', flat=True):
            instance.products.add(product_id)
        if status is not None:
            instance.closed = status
            instance.save()
        return instance
