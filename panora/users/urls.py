from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/',views.register_view,name='register-user'),
    path('login/',views.login_view,name='login-user'),
    path('logout/',views.logout_view,name='logout-user'),
]

