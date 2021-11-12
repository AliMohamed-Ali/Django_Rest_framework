from django.contrib import admin
from .models import Movie,Series,Category

# Register your models here.
admin.site.register(Movie)
admin.site.register(Series)
admin.site.register(Category)