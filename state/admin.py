from django.contrib import admin
from django.contrib import messages
from . models import State


class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'created_on')

    def active(self, obj):
        return obj.is_active == 1
    active.boolean = True

    def make_active(modeadmin, request, queryset):
        queryset.update(is_active = 1)
        messages.success(request, "Selected Record(s) Marked as Active")

    def make_inactive(modeadmin, request, queryset):
        queryset.update(is_active = 0)
        messages.success(request, "Selected Record(s) Marked as Inactive")
    
    def has_delete_permission(self, request, obj=None): #Add/ Remove according to the User Permissions
        return False
    
    def has_add_permission(self, request): #Add/ Remove according to the User Permissions
        return False
    
    admin.site.add_action(make_active, "Make Active")
    admin.site.add_action(make_inactive, "Make Inactive")
admin.site.register(State, StateAdmin)