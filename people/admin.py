from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.utils.translation import ugettext, ugettext_lazy as _
from .models import Child, Family, Parent, Leader

ADDRESSFIELDSET = [
    ('Address', {
        'fields': ('address', 
                  ('city', 'state', 'zip'))
    })
]

CONTACTFIELDSET = [
    ('Contact Information', {
        'fields': (('phone', 'email'),)
    })
]

NAMEFIELDSET = [
    (None, {
        'fields': (('first_name', 'last_name'),)
    })
]

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    _ADDRESSFIELDSET = ADDRESSFIELDSET.copy()
    _ADDRESSFIELDSET[0][1]['classes'] = ('collapse',)

    fieldsets = [(
        None, {
            'fields': (('first_name', 'last_name', 'family'),)
        })] + _ADDRESSFIELDSET + CONTACTFIELDSET + [
        ('Preferred Contact Methods', {
            'fields': (('prefer_phone', 'prefer_email'),)
        }),
    ]
    list_display = ('full_name', 'family')
    list_filter = (('family', admin.RelatedOnlyFieldListFilter),)
    

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name', 'family__slug')
    readonly_fields = ('age','official_age')
    fieldsets = (
        (None, {
            'fields': (
                ('first_name', 'last_name', 'family'),
                ('dob', 'age', 'official_age'),
                ('gender', 'grade'),
            )
        }),
        ('Assignment Info', {
            'fields': (
                ('group', 'color'),
                ('guest', 'guest_of')
            )
        }),
        ('Safety Information', {
            'fields': (
                ('allergies', 'medications'),
                'special_instructions',
                ('photo_release', 'medical_release'),
                'notes'
            )
        })
    )

    list_display = ('first_name', 'last_name', 'guest', 'family', 'grade', 'official_age', 'group', 'color')
    list_editable = ('group', 'color', 'family',)
    list_filter = ('group', 'guest')


@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display = ('slug', 'children_short', 'parents_short')
    fieldsets = ADDRESSFIELDSET + [
        ('Church Info', {
            'fields': (('attend_church', 'church_name'),)
        }),
        ('Emergency Contact',{
            'fields': (('ICEContactName', 'ICEContactPhone'),)
        }),
        ('Pickup List', {
            'fields': ('pickup',)
        }),
        ('slug', {
            'fields': ('slug',),
            'classes': ('collapse',)
        })
    ]

    def update_slug(modeladmin, request, queryset):
        queryset.update(slug='')
        for f in queryset:
            f.save()
    update_slug.short_description = "Update family name"

    actions = [update_slug]

class LeaderChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Leader

@admin.register(Leader)
class LeaderAdmin(UserAdmin):
    fieldsets = NAMEFIELDSET + ADDRESSFIELDSET + CONTACTFIELDSET + [
        ('Leader Info', {
            'fields': (('position', 'group'),
                        'cpp',
                        'parent')
        }),
        ('Admin Info', {
            'fields': (('username', 'password'),),
            'classes': ('collapse',)
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 
                       'is_superuser', 'groups', 
                       'user_permissions'),
            'classes': ('collapse',)
        }),
        (_('Important dates'), {
            'fields': ('last_login', 'date_joined'),
            'classes': ('collapse',)
        })
        ]
        