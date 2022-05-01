from django.contrib import admin

from .models import BugDescription, SolvingStatus

admin.site.register(BugDescription)
admin.site.register(SolvingStatus)
