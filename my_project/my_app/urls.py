from django.urls import path
from . import views
from .views import ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView

urlpatterns = [
	path('', views.home, name='home'),
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
]