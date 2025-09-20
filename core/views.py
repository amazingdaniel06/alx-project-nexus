from rest_framework import viewsets, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
filterset_fields = ['category']            # filter by category
ordering_fields = ['price', 'name', 'created_at']  # sortable fields
search_fields = ['name', 'description']    # search by name/description