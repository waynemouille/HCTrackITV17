from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include ('articles.urls')),
    path('tickets/', include ('tickets.urls')),
    path('projects/', include ('projects.urls')),

]
