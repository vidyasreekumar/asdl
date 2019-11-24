from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('dashboard', views.login, name='dashboard'),

    path('logout', views.logout, name='logout'),
]


from django.urls import path
from . import views

urlpatterns = [
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout, name="logout"),
    path("result", views.result, name="result"),
    path("pay", views.pay, name="pay"),
    path("reval", views.reval, name="reval"),
]



