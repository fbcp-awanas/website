from django.contrib import admin
from django.utils.translation import ugettext, ugettext_lazy as _
from .models import Group

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = 'name club age'.split()
    list_filter = ['club', ]
    filter_horizontal = ['leaders',]