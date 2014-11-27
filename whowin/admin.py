from django.contrib import admin
from whowin.models import Fighter, Fight


class FightAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'end', 'user')
    readonly_fields = ('end',)

admin.site.register(Fighter)
admin.site.register(Fight, FightAdmin)
