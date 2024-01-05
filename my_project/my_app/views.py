from django.http import HttpResponse
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from .helper import backgroundTask


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        print("perform_create")

        instance = serializer.save()
        product_id = instance.id
        backgroundTask.delay(product_id, 'created')


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_update(self, serializer):
        print("perform_update")
        instance = serializer.save()
        product_id = instance.id
        backgroundTask.delay(product_id, 'updated')


def home(request):
    html = "<html><body><h1>Hello!</h1></body></html>"
    return HttpResponse(html)
