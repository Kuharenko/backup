from django.contrib import admin
from models import Blog

# Register your models here.

admin.autodiscover()

admin.site.register(Blog)
