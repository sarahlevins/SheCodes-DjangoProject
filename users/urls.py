from django.urls import path, include, re_path
from users.views import RegisterSuccessView
from . import views

app_name = 'users'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.register, name='register'),
    path('accounts/register/success/',
         RegisterSuccessView.as_view(), name='register_success'),
    path('accounts/update_profile/', views.update_profile, name='update_profile'),
    path('<int:pk>/', views.ProfileView.as_view(), name='profile'),

    # path('<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    # path('<int:pk>/update_account', views.UserUpdate.as_view(), name='user-update'),
    # path('<int:pk>/delete_account', views.UserDelete.as_view(), name='user-delete'),
]
