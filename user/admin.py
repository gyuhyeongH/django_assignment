from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.


class UserProfileInline(admin.StackedInline):
    model = UserProfile


class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username',]
    list_display = ['username']
    list_filter = ('username',)
    search_fields = ('username')
    filter_horizontal = []
    inlines = (UserProfileInline,)
    fieldsets = (
        ("info", {"fields": ('username','password')}),
        ('Permissions',{'fields':('is_admin','is_active')}),
    )
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('username')
        else:
            return ('join_date',)


admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Hobby)

