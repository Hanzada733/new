from django.urls import path

from first import views

urlpatterns = [
    path('',views.IndexView.as_view())
]
