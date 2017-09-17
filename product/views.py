import datetime

from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import View

from product.models import Invoice, Product


class InvoiceView(View):

    def get(self, request):
        context = {}
        today = datetime.datetime.now().date()
        context['today'] = today
        invoices = Invoice.objects.filter(created=today).order_by('-created')
        context['invoices'] = invoices
        products = Product.objects.all().order_by('name')
        context['products'] = products
        User = get_user_model()
        users = User.objects.exclude(invoices__in=invoices)
        context['users'] = users
        count_products = {}
        total = 0
        for invoice in invoices:
            for product in invoice.products.all():
                if product.name in count_products:
                    count_products[product.name][0] += 1
                    count_products[product.name][1] += product.price
                    total += product.price
                else:
                    count_products[product.name] = [1, product.price]
                    total += product.price
        context['count_products'] = count_products
        context['total'] = total
        return render(request, 'pages/home.html', context)
