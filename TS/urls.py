from os import name
from . import views
from django.urls import path


urlpatterns=[
    path('',views.PredictiveCount,name='PredictiveCount'),
    path('Realdata',views.Realdata,name='Realdata'),
    path('generatepredection/', views.generatePredection, name='generatepredection'),
    path('allstoreprediction/', views.allstoreprediction, name='allstoreprediction'),
    # CART AJAX
    path('get_chart_storewise/', views.get_chart_storewise, name='get_chart_storewise'),
    path('allstorepredictionChart/', views.allstorepredictionChart, name='allstorepredictionChart'),
    path('exportstoresTS/', views.export_stores_xlsTS , name='exportstoresTS'),
    path('importstoresTS/', views.import_stores_xlsTS , name='importstoresTS'),
    path('<int:pk>/edit', views.update_misdata, name='update_misdata'),
    path('<int:pk>/delete', views.delete_misdata, name='delete_misdata'),
    path('delete_all_mis_data',views.delete_all_mis_data,name='delete_all_mis_data'),
    path('generateData',views.generateData,name='generateData')
] 