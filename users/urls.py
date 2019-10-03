from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.Register.as_view() , name='user-create'),
    path('login/', views.Login.as_view() , name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('<int:pk>/update_account', views.UserUpdate.as_view(), name='user-update'),
]