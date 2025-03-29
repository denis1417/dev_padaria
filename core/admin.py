from django.contrib import admin

from .models import Produto


class ProdutoAdmin(admin.ModelAdmin):
    list_display=('produto','lote','validade')


admin.site.register(Produto,ProdutoAdmin)

