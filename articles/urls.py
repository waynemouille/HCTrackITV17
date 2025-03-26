from django.urls import path
from . import views

urlpatterns = [
    path('', views.knowledgebaseHome, name='knowledgebase_home'),
    path('knowledgebase_createnew/', views.knowledgebaseCreatenew, name='knowledgebase_createnew'),

    path('knowledgebase_info/<str:pk>', views.knowledgebaseInfo, name='knowledgebase_info'),
    path('knowledgebase_delete/<str:pk>', views.knowledgebaseDelete, name="knowledgebase_delete"),
    path('knowledgebase_edit/<str:pk>', views.knowledgebaseEdit, name="knowledgebase_edit"),
]