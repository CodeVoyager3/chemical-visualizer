from django.urls import path
from .views import FileUploadView
from .views import FileUploadView, generate_pdf

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('export-pdf/<int:batch_id>/', generate_pdf, name='export-pdf'),
]