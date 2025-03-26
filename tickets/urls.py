from django.urls import path
from . import views

urlpatterns = [
    #path('', views.ticketsDashboard, name='tickets_dashboard'),
    path('', views.ticketsHome, name='tickets_home'),
    path('login/', views.loginMain, name='login'),
    path('tickets_current/', views.ticketsCurrent, name='tickets_current'),
    path('tickets_onhold/', views.ticketsOnhold, name='tickets_onhold'),
    path('tickets_completed/', views.ticketsCompleted, name='tickets_completed'),
    path('tickets_createnew/', views.ticketsCreatenew, name='tickets_createnew'),
    path('logout/', views.logoutUser, name="logout"),
    path('confirmation/', views.confirmation, name="confirmation"),
    path('credentials/', views.credentials, name="credentials"),
    path('support_directory/', views.supportDirectory, name="support_directory"),
    path('user_dashboard/', views.userdashboardPage, name="user_dashboard"),



    
    path('tickets_info/<str:pk>', views.ticketsInfo, name='tickets_info'),
    path('delete/<str:pk>', views.ticketsDelete, name="tickets_delete"),
    path('tickets_update_update/<str:pk>', views.ticketsUpdate, name="tickets_update_update"),
    path('tickets_update_complete/<str:pk>', views.completeTicket, name="tickets_update_complete"),
    path('tickets_info_completed/<str:pk>', views.ticketsCompletedinfo, name="tickets_info_completed"),





]