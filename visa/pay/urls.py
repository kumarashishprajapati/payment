from django.contrib import admin
from django.urls import path
from . import views
admin.site.site_header = "VISA Admin"
admin.site.site_title = "VISA Admin Portal"
admin.site.index_title = "Welcome to VISA Researcher Portal"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name=""),
]