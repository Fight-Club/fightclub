from django.contrib import admin
from whowin.models import Fighter, Fight


class FightAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'end', 'user')
    readonly_fields = ('end',)
    actions_on_bottom = True
    actions_on_top = False


class FighterAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'rating')
    ordering = ('-rating',)
    actions_on_bottom = True
    actions_on_top = False


admin.site.register(Fighter, FighterAdmin)
admin.site.register(Fight, FightAdmin)
