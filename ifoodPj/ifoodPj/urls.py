from ifoodApp import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),
    path('cad/',views.cad, name="cad"),
    path('pedido/',views.pedido, name="pedido"),
    path('platform/',views.platform, name="platform"),
    path('pizza',views.pizza, name="pizza"),
    path('temaki_salmao',views.temaki_salmao, name="temaki_salmao"),
    path('sorvete',views.sorvete, name="sorvete"),
    path('bolo',views.bolo, name="bolo"),
    path('esfiha',views.esfiha, name="esfiha"),
    path('coca_cola',views.coca_cola, name="coca_cola"),
    path('rec_password',views.rec_password, name="rec_password"),
    path('confirm_email',views.confirm_email, name="confirm_email"),
]
