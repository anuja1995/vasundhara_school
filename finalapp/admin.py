from django.contrib import admin
from .models import Student_Details,Section_Master,Classes_Master
# Register your models here.
admin.site.register(Student_Details)
admin.site.register(Section_Master)
admin.site.register(Classes_Master)