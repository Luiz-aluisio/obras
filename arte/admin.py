from django.contrib import admin, messages
from django.urls import reverse
from django.utils.html import format_html
from .models import Autor, Obra


admin.site.disable_action('delete_selected')


def related_links(obj, attr):
    links = []
    all = getattr(obj, attr).all()
    for related_obj in all:
        change = (
            f'admin:{related_obj._meta.app_label}'
            f'_{related_obj._meta.model_name}_change'
        )
        url = reverse(change, args=[related_obj.id])
        links.append(f'<a href="{url}">{related_obj}</a>')

    return format_html('<br>'.join(links))


class ObraInline(admin.TabularInline):
    model = Obra.autores.through


class AutorInline(admin.TabularInline):
    model = Autor.obras.through


@admin.register(Obra)
class ObraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'id', 'autores_links')
    actions = ['delete_selected']
    exclude = ['autores']
    inlines = [AutorInline]

    def autores_links(self, obj):
        return related_links(obj, 'autores')


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'id', 'obras_links')
    inlines = [ObraInline]

    def obras_links(self, obj):
        return related_links(obj, 'obras')

    def delete_view(self, request, object_id, extra_context=None):
        obj = self.get_object(request, object_id)

        if obj.obras.exists():
            self.message_user(
                request,
                'autor não pode ser excluido pois possui obras',
                level=messages.ERROR,
            )
            return self.change_view(request, object_id, extra_context)

        return super().delete_view(request, object_id, extra_context)
