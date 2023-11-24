from django.urls import path
from .views import home, cat_info

urlpatterns = [
    path('', home, name='home'),
    path('cat_info/<int:cat_id>/', cat_info, name='cat_info'),
]
