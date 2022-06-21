from django.contrib import admin
from .models import *
# Register your models here.


class UserProfileInline(admin.StackedInline):
    model = UserProfile

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'hobby':
            kwargs['queryset'] = Hobby.objects.filter(id__lte=7)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class UserAdmin(admin.ModelAdmin):
    inlines = (
        UserProfileInline,
    )


admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Hobby)

