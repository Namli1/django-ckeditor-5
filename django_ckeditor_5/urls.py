from django.urls import path
from . import views

urlpatterns = [
    path("image_upload/", views.upload_file, name="upload_file"),
    path("image_delete/<path:path>", views.delete_file, name="delete_file"),
]