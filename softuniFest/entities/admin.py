from django.contrib import admin

from .models import *


class UserAdmin(admin.ModelAdmin):
    """Users read-only admin interface."""

    list_display = [
        'first_name',
        'last_name',
        'department',
        'position'
        ]

    fieldsets = [
        ('General',
         {'fields': ['email',
                     'first_name',
                     'middle_name',
                     'last_name',
                     'phone_number',
                     'department',
                     'position',
                     'is_staff',
                     'is_active'] }),

    ]

class DepartmentAdmin(admin.ModelAdmin):
    """Users read-only admin interface."""

    list_display = [
        'name'
        ]

class NewsAdmin(admin.ModelAdmin):
    """Users read-only admin interface."""

    list_display = [
        'title',
        'date'
        ]

class PositionAdmin(admin.ModelAdmin):
    """Users read-only admin interface."""

    list_display = [
        'name',
        'available'
        ]



admin.site.register(User, UserAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(News, NewsAdmin)
