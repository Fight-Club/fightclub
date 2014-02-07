from django.contrib import admin
from whowin.models import Fighter, Fight

admin.site.register(Fighter, Fight)