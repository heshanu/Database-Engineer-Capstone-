from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('',views.home,name="home"),
    path('menu/',views.menu,name="menu"),
    path('message/', views.msg),
    path('secrect/',views.secrect),
    path('api-token-auth',obtain_auth_token),
    path('throttle-check',views.throttle_check),
    path('throttle-check-auth',views.throttle_check_auth),
    path('groups/manager/users',views.manager),
    path('me/',views.me),
    path('manager-view/',views.manager_view),
    path('menu-items', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
]