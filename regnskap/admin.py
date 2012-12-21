from django.contrib import admin
from django_regnskap.regnskap.models import *

class BilagAdmin(admin.ModelAdmin):
    list_display = ('bilagsnummer', 'dato',) # 'innslag')
#    filter_horizontal = ('innslag',)

class KontoAdmin(admin.ModelAdmin):
    class Meta:
        model = Konto
    list_display = ('nummer','prosjekt', 'tittel', 'kontoType')
    list_filter = ('prosjekt', 'kontoType')
    exclude = ('kontoType',)

#admin.site.register(Bilag, BilagAdmin)
#admin.site.register(Innslag)
admin.site.register(Konto, KontoAdmin)
admin.site.register(Exteral_Actor)
admin.site.register(Prosjekt)