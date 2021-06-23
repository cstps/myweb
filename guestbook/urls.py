from django.urls import path
from guestbook import views


urlpatterns =[
    path('',views.list),
    path('write', views.write),
    path('gb_insert', views.gb_insert),
    path('passwd_check',views.passwd_check),
    path('gb_detail',views.gb_detail),
    path('gb_update',views.gb_update),
    path('gb_delete',views.gb_delete),
]