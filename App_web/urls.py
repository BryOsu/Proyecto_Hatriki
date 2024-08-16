from django.urls import path
from .views import *

urlpatterns = [
    path('About-us/',Aboutus.as_view(), name='About-us'),
    path('', HomeView.as_view(), name='start'),
    path('kits/<int:product_id>/', KitsView, name='kits'),
    ]