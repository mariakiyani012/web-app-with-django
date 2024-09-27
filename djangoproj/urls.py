from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Digitalux Admin"
admin.site.site_title = "Digitalux Admin Portal"
admin.site.index_title = "Welcome to Digitalux"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))
]
