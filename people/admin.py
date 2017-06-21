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


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    fieldsets = [(
        None, {
            'fields': (('first_name', 'last_name', 'family'),)
        })] + [
        ('Address', {
            'fields': ('address', 
                      ('city', 'state', 'zip')),
            'classes': ('collapse',)
        })
    ] + CONTACTFIELDSET + [
        ('Preferred Contact Methods', {
            'fields': (('prefer_phone', 'prefer_email'),)
        }),
    ]
    list_display = ('full_name', 'family')
    list_filter = (('family', admin.RelatedOnlyFieldListFilter),)
    

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    class ClubFilter(admin.SimpleListFilter):
        title = _('Club')
        parameter_name = 'club'

        def lookups(self, request, model_admin):
            return (
                ('awanas', 'Awanas'),
                ('puggles', 'Puggles'),
                ('cubbies', 'Cubbies'),
                ('sparks', 'Sparks'),
                ('tnt', 'Truth & Training')
            )
        
        def queryset(self, request, queryset):
            if self.value() == 'awanas':
                return queryset.filter(group__club='A')
            if self.value() == 'puggles':
                return queryset.filter(group__club='P')
            if self.value() == 'cubbies':
                return queryset.filter(group__club='C')
            if self.value() == 'sparks':
                return queryset.filter(group__club='S')
            if self.value() == 'tnt':
                return queryset.filter(group__club='T')

    
    search_fields = ('first_name', 'last_name', 'family__slug')
    readonly_fields = ('age', 'official_age', 'club')
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
    list_filter = (('group', admin.RelatedOnlyFieldListFilter),
                   ClubFilter, 
                   'guest')


class LeaderChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Leader

@admin.register(Leader)
class LeaderAdmin(UserAdmin):
    fieldsets = NAMEFIELDSET + ADDRESSFIELDSET + CONTACTFIELDSET + [
        ('Leader Info', {
            'fields': (('position'),
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
    
    # list_filter = (('group', admin.RelatedOnlyFieldListFilter),)
        