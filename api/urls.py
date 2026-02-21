from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import CategoryViewSet, TransactionViewSet, SummaryView

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'transactions', TransactionViewSet, basename='transaction')

urlpatterns = [
    # path('login/', TokenObtainPairView.as_view(), name='login'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('summary/', SummaryView.as_view(), name='summary'),
    path('', include(router.urls)),
]