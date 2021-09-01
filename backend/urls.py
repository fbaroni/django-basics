from django.urls import path
import backend.views as views

urlpatterns = [
    path('', views.index, name='backend_index'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('json/', views.get_json, name='get_json'),
]
