from django import forms
from ards_site.models import Member, Batting


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
