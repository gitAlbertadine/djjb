from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.JobList.as_view(), name='job_list'),
    path('<int:pk>', views.JobDetail.as_view()),

]
