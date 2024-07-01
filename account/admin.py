from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class CustomUserAdminForm(forms.ModelForm):
    is_active = forms.BooleanField(label='Active', required=False, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')
    is_staff = forms.BooleanField(label='Admin login', required=False, help_text='Designates whether the user can log into this admin site.')
    is_student= forms.BooleanField(label='Student', required=False, help_text='Designates whether the user is a student.')
    is_employee = forms.BooleanField(label='Employee', required=False, help_text='Designates whether the user is an employee.')
  
    class Meta:
        model = User
        fields = '__all__'

class CustomUserAdmin(BaseUserAdmin):
    model = User
    form = CustomUserAdminForm

    # Cfields displayed in the admin interface
    fieldsets = (
        (None, {'fields': ('id','username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email','profile_image')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', )}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Custom fields', {'fields': ('is_admin', 'is_student', 'is_employee', 'is_approved', 'approve_login')}),
    )

    #  admin actions
    actions = ['approve_users', 'confirm_email']

    # Admin action to approve selected users
    def approve_users(self, request, queryset):
        queryset.update(is_approved=True)
    approve_users.short_description = "Approve selected users"

    # Admin action to confirm email and activate accounts
    def confirm_email(self, request, queryset):
        for user in queryset:
            user.email_confirmed = True
            user.is_active = True
            user.save()
    confirm_email.short_description = "Confirm email and activate accounts"

    # Make only approve_login and permissions fields editable
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return [f.name for f in self.model._meta.fields if f.name not in ('approve_login', 'is_active', 'is_staff', 'is_superuser')]
        return []

    # Save model method
    def save_model(self, request, obj, form, change):
        if obj.approve_login:
            obj.is_approved = True
        
        obj.status = self.custom_staff_status(obj)
        
        obj.save()

    #  displayed in the admin interface
    list_display = ('id','username', 'email', 'first_name', 'last_name', 'is_superuser' ,'is_active', 'is_student', 'is_employee','is_admin','profile_image')
 
    def custom_staff_status(self, obj):
        if obj.is_active and obj.is_staff:
            return 'Active Staff'  
        elif obj.is_active:
            return 'Active'  
        else:
            return 'Inactive'

# Register the custom UserAdmin class
admin.site.register(User, CustomUserAdmin)