from django.urls import path

from app.views import Template

urlpatterns = [
    path('', Template.as_view())
]
