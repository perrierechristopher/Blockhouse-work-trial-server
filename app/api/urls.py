from django.urls import path
from .views import get_chart_data

urlpatterns = [
    path("line-chart-data/", get_chart_data, name="get_chart_data"),
    path("bar-chart-data/", get_chart_data, name="get_chart_data"),
    path("pie-chart-data/", get_chart_data, name="get_chart_data"),
]