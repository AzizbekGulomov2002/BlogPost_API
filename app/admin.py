from django.contrib import admin

# Register your models here.
from .models import BlogPost

class BlogPost_Admin(admin.ModelAdmin):
    list_display = ['nomi','maqola_soni','sana']
    list_per_page = 10
    ordering = ('nomi','maqola_soni','sana')
    search_fields = ['nomi','maqola_soni','sana']
admin.site.register(BlogPost, BlogPost_Admin)