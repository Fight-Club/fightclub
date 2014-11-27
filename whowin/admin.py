from django.contrib import admin
from whowin.models import Fighter, Fight


class FightAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'end', 'user')
    readonly_fields = ('end',)


class FighterAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'rating')
    ordering = ('-rating',)


admin.site.register(Fighter, FighterAdmin)
admin.site.register(Fight, FightAdmin)
