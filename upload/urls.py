from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('upload/', views.upload_document, name='upload_document'),
    path('', views.document_list, name='document_list'),
    path('delete/<int:document_id>/', views.delete_document, name='delete_document'),
]
