from django.urls import path

from . import views

app_name = "bill"

urlpatterns = [
    # Create
    path("add/", views.AddView.as_view(), name="add"),
    # Retrieve
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # Update
    path("<int:pk>/update/", views.UpdateView.as_view(), name="update"),
    # Delete
    path("<int:pk>/delete/", views.DeleteView.as_view(), name="delete"),

]
