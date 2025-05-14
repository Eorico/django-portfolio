from django.urls import path
from . import views

urlpatterns = [
    path('', views.mamba, name='mamba'),
    path('KnowMeWell', views.IgTrend, name="IgTrend"),
    path('FindCrewmates', views.Searchpage.as_view() , name="SearchPage"),
    path('ORMTable', views.ORMTable, name="ORMTable"),
]
