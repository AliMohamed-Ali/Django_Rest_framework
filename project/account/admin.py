from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.contrib.auth.forms import UserChangeForm


class UserAdminForm(UserChangeForm):
    class Meta:
        fields = '__all__'


class CustomUserAdmin(UserAdmin):
    form = UserAdminForm
    list_display = ('username', 'first_name', 'last_name', 'is_staff', 'mobile')
    fieldsets = (
        ('Generic Info', {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name','mobile','profile_image')}),
        (None, {'fields': ('is_active', 'is_staff', 'is_superuser', )}),
    )


admin.site.register(User, CustomUserAdmin)
