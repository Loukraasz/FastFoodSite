from ifoodApp import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),
    path('cad/',views.cad, name="cad"),
    path('pedido/',views.pedido, name="pedido"),
    path('login/',views.login, name="login"),
]
