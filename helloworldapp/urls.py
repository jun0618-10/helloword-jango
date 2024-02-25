from django.contrib import admin
from django.urls import path,include
from .views import helloworldappview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworldapp/',helloworldappview)
]
