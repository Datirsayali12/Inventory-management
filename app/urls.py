from django.urls import path
from .views import create_item, get_item, update_item, delete_item
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('items/', create_item, name='create_item'),
    path('items/<int:item_id>/', get_item, name='get_item'),
    path('items/<int:item_id>/update/', update_item, name='update_item'),
    path('items/<int:item_id>/delete/', delete_item, name='delete_item'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]