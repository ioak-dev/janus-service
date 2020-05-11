from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns =[
    path('', views.get_update_stage),
    path('<str:project_id>/move', views.move_stage),
    path('<str:id>', views.by_id)
]