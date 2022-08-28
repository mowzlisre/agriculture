from django.urls import path
from . import views

urlpatterns = [
    path('api/getAll', views.GetAllAPIView.as_view()),
    path('api/newRecord', views.AddRecordAPIView.as_view())
]