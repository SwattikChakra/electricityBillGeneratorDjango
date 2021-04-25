from django.urls import path

from . import views

app_name = "bill"

urlpatterns = [
    # Create
    path("add/", views.AddView.as_view(), name="add"),
    # Read
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
]
