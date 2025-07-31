from django.urls import path
from todos import views

urlpatterns = [
    path("",views.todofn,name="todo"),
    path("apitodo/",views.apitodo,name="apitodo"),
    path("apiedittodo/<int:t_id>/",views.apiedittodo,name="apiedittodo"),
    path("apideletetodo/<int:t_id>/",views.apideletetodo,name="apideletetodo"),
    path("manualapiedit/<int:id>/",views.manualapiedit,name="manualapiedit"),
    path("manualapidelete/<int:id>/",views.manualapidelete,name="manualapidelete"),
]
