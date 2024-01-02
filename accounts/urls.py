from django.urls import path

from accounts.views import UserDetailView


app_name = "accounts"
urlpatterns = [
    path('api/user/<int:pk>/', UserDetailView.as_view(), name='user-detail')
]