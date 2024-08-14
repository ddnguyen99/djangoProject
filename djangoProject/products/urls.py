from django.urls import path

from products.views import ProductDetailAPIView, ProductListCreateAPIView

urlpatterns = [
	path('', ProductListCreateAPIView.as_view(), name = 'product_create'),
	path('<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail'),
]