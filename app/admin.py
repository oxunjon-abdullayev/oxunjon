from django.contrib import admin

# Register your models here.
from app.models import Blog, Contact, Skills

admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(Skills)
