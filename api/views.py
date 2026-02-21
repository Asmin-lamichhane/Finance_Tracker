from rest_framework import viewsets, permissions, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
# from django_filters.rest_framework import DjangoFilterBackend

from .models import Category, Transaction
from .serializers import CategorySerializer, TransactionSerializer


#Category ViewSet

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Category.objects.all()


#Transaction ViewSet

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # filterset_fields = ['transaction_type', 'category']
    # search_fields = ['description']
    permission_classes = [permissions.AllowAny]

    # def get_queryset(self):
    #     return Transaction.objects.filter(
    #         user=self.request.user
    #     ).select_related('category', 'user').order_by('-date')

    # def perform_create(self, serializer):
    #     # Automatically attach logged-in user on create
    #     serializer.save(user=self.request.user)


#Summary View

class SummaryView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    

    def get(self, request):
        qs = Transaction.objects.filter(user=request.user)

        total_income = qs.filter(
            transaction_type='INCOME'
        ).aggregate(total=Sum('amount'))['total'] or 0

        total_expenses = qs.filter(
            transaction_type='EXPENSE'
        ).aggregate(total=Sum('amount'))['total'] or 0

        return Response({
            'total_income': total_income,
            'total_expenses': total_expenses,
            'net_balance': total_income - total_expenses,
        })