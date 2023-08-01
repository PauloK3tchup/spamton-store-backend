from django.contrib import admin

from .models import Categoria, Produto, Imagem


class ImagemAdmin(admin.StackedInline):
    model = Imagem


class ProdutoAdmin(admin.ModelAdmin):
    inlines = [ImagemAdmin]

    class Meta:
        model = Produto


admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Imagem)
