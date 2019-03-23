from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):

    list_display = ['title', 'puplishing_date', 'slug'] # Başlıkları eklemek için
    list_display_links = ['puplishing_date'] # Başlıkların tıklanabilmek için
    list_filter = ['puplishing_date'] # sayfaya filtre eklemek için
    search_fields = ['title', 'content'] # sayfaya arama alanı eklemek için.
    list_editable = ['title'] # başlıkların editlenmesi için

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
