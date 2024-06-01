from django.urls import path
from . import views

urlpatterns = [
    # as_view() renders the MenuList
    path('', views.MenuList.as_view(), name="home"),
    path('item/<int:pk>/', views.MenuItemDetail.as_view(), name="menu_item"),
]