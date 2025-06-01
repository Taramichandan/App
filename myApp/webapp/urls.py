from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('register/',views.register_view,name='register'),
    path('client/<int:pk>',views.client,name='client'),
    path('client_delet/<int:pk>',views.client_delet,name='client_delet'),
    path('client_update/<int:pk>',views.client_update,name='client_update'),
    path('add_client/',views.add_client,name='add_client'),
]
 