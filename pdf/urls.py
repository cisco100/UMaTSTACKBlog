from django.urls import path
from pdf.views import pdf_report_create
urlpatterns = [
    
    path('<slug:category_slug>/<slug:slug>/', pdf_report_create, name='create-pdf'),
    

    ]