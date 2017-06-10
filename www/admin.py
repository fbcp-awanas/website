from django.contrib import admin
from .models import Parent, Clubber, Family, Leader, Visitor,
                    Club, Handbook, Section, Inventory,
                    Awards, Points, Activity, Attendance, Finance, Expense

# Register your models here.

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    pass

@admin.register(Clubber)
class ClubberAdmin(admin.ModelAdmin):
    pass

@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    pass

@admin.register(Leader)
class LeaderAdmin(admin.ModelAdmin):
    pass

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    pass

@admin.register(Club)
class ClubAdmin(models.ModelAdmin):
    pass

@admin.register(Handbook)
class HandbookAdmin(models.ModelAdmin):
    pass

@admin.register(Section)
class SectionAdmin(models.ModelAdmin):
    pass

@admin.register(Inventory)
class InventoryAdmin(models.ModelAdmin):
    pass

@admin.register(Awards)
class AwardsAdmin(models.ModelAdmin):
    pass

@admin.register(Points)
class PointsAdmin(models.ModelAdmin):
    pass

@admin.register(Activity)
class ActivityAdmin(models.ModelAdmin):
    pass

@admin.register(Attendance)
class AttendanceAdmin(models.ModelAdmin):
    pass

@admin.register(Finance)
class FinanceAdmin(models.ModelAdmin):
    pass

@admin.register(Expense)
class ExpenseAdmin(models.ModelAdmin):
    pass