from django.contrib import admin

# Register your models here.
from .models import Produtos
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'quantidade',)
    list_filter = ('preco',)
    search_fields = ('nome',)
admin.site.register(Produtos, ProdutoAdmin)