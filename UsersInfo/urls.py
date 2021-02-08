from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('schemas', views.schemas),
    path('schemas/newSchema', views.add_new_schema),
    path('home', views.index),
    path('home/<int:pk>/update', views.UpdateScheme.as_view()),
    path('home/<int:pk>/delete', views.DeleteSchema.as_view()),
    path('login', views.user_login),
    path('logout', views.user_logout),
    path('register', views.user_register),
    path('home/<int:pk>/export', views.export_to_csv)
]
