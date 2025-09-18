from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile

# Personalizar el admin de UserProfile
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email', 'phone', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'first_name', 'last_name', 'email')
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ('Información Personal', {
            'fields': ('user', 'first_name', 'last_name', 'email', 'phone')
        }),
        ('Información del Sistema', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

# Personalizar el admin de User para mostrar información del perfil
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Perfil'

class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined')
    list_filter = UserAdmin.list_filter + ('userprofile__created_at',)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
