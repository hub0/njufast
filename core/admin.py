from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core.models import User

from .forms import UserCreationForm, UserChangeForm




class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # fields to display in admin page
    list_display = ('email', 'is_admin', 'is_active')
    # fields to filter in admin page
    list_filter = ('is_admin', )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

    # display in user info page
    fieldsets = (
        #('Info', {'fields': ('name',)}),
        ('Authentication', {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_active')}),
    )

    # display in create user page
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )



# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
