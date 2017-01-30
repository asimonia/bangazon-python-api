from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import *
from api.models import customer, paymenttype, product, order, orderproduct


class OrderProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Orders to be viewed or edited.
    """
    queryset = orderproduct.OrderProduct.objects.all()
    serializer_class = OrderProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Orders to be viewed or edited.
    """
    queryset = order.Order.objects.all()
    serializer_class = OrderSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Products to be viewed or edited.
    """
    queryset = product.Product.objects.all()
    serializer_class = ProductSerializer


class ProductTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ProductTypes to be viewed or edited.
    """
    queryset = product.ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class PaymentTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows PaymentTypes to be viewed or edited.
    """
    queryset = paymenttype.PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Customers to be viewed or edited.
    """
    queryset = customer.Customer.objects.all().order_by('-created')
    serializer_class = CustomerSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer