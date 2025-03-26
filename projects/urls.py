from django.urls import path
from . import views

urlpatterns = [
    path('', views.projectsHome, name='projects_home'),
    path('projects_completed/', views.projectsCompleted, name="projects_completed"),
    path('projects_createnew', views.projectsCreatenew, name="projects_createnew"),


    path('projects_info/<str:pk>', views.projectsInfo, name='projects_info'),
    path('projects_update_update/<str:pk>', views.projectsUpdate, name="projects_update_update"),
    path('projects_update_complete/<str:pk>', views.completeProject, name="projects_update_complete"),
    path('projects_info_completed/<str:pk>', views.projectsCompletedinfo, name="projects_info_completed"),
]