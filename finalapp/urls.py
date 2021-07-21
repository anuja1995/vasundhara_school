from django.contrib import admin
from django.urls import path
from .views import StudentDetailsView


urlpatterns = [
    path('StudentDetailsView/', StudentDetailsView, name='StudentDetailsView'),
    # path('StudentDetailsView_demo/', StudentDetailsView_demo, name='StudentDetailsView_demo'),

    # path('render_pdf_view/', render_pdf_view, name='render_pdf_view'),

    # path('GeneratePDF/', GeneratePDF.as_view(), name='GeneratePDF'),
    # path('display/', StudentDetailsView, name='pdf'),
    # path('student_view/', student_view, name='student_view'),
]
