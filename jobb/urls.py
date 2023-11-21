from django.urls import path, include
from . import views
from . import api


app_name = 'jobb'

urlpatterns = [
    path('',views.job_list,name="job_list"),
    path('add',views.add_job,name="add_job"),
    path('<str:slug>',views.job_detail,name="job_detail"),
    
    
    
    ## api
    path('api/list',api.job_list_api,name="job_list_api"),
    path('api/list/<int:id>',api.job_detail_api,name="job_detail_api"),

    ## class based views 
    path('api/v2/list',api.JobListApi.as_view(),name="JobListApi"),
    path('api/v2/list/<int:id>',api.JobDetailApi.as_view(),name="job_detail_api"),
    
]