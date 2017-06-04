from django.contrib import admin
from.models import Clubber, Adult, Family
# Register your models here.

@admin.register(Adult)
class AdultAdmin(admin.ModelAdmin):
    pass

@admin.register(Clubber)
class ClubberAdmin(admin.ModelAdmin):
    pass

@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    pass
