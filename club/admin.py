from django.contrib import admin
from django.utils.translation import ugettext, ugettext_lazy as _
from .models import Group, Handbook, Section

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = 'name club age grades'.split()
    list_filter = ['club', ]
    filter_horizontal = ['leaders',]

@admin.register(Handbook)
class HandbookAdmin(admin.ModelAdmin):
    pass

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass