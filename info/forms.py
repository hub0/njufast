from django import forms
from .models import TeamMember

class MemberUpdateForm(forms.ModelForm):
    """
    A form for updating members' name and affiliation by users
    """
    class Meta:
        model = TeamMember
        fields = ['name', 'affiliation']
