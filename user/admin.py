from django import forms

from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.


class UserProfileInline(admin.TabularInline):
    model = UserProfile
    filter_horizontal= ['hobby']

class UserAdmin(BaseUserAdmin):
    list_display = ['id','username',]
    list_display = ['username']
    list_filter = ('username',)
    search_fields = ('username','email',)
    filter_horizontal = []

    fieldsets = (
        ("info", {"fields": ('username','password','email','fullname')}),
        ('Permissions',{'fields':('is_admin','is_active')}),
    )
    inlines = (
        UserProfileInline,
    )
    add_fieldsets= (
    (None, {
        'classes':('wide',),
        'fields': ('email', 'fullname', 'password1','password2')}
    ),

    )
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('username')
        else:
            return ('join_date',)
        
    
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)
admin.site.register(Hobby)

