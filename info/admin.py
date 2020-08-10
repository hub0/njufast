from django.contrib import admin
from .models import Affiliation, TeamMember

class AffiliationAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation')
    ordering = ('name', 'abbreviation')

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('get_name', 'get_email', 'get_affiliation')
    search_field = ('get_name', 'get_email')
    #ordering = ('get_name', 'get_email', 'get_affiliation')

    def get_name(self, obj):
        return obj.user.name
    get_name.admin_order_field = 'user__name'
    get_name.short_description = 'Full Name'

    def get_email(self, obj):
        return obj.user.email
    get_email.admin_order_field = 'user__email'
    get_email.short_description = 'Email'

    def get_affiliation(self, obj):
        return obj.affiliation.abbreviation
    get_affiliation.admin_order_field = 'affiliation__abbreviation'
    get_affiliation.short_description = 'Affiliation'
    


admin.site.register(Affiliation, AffiliationAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
