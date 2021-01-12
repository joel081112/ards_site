from django import forms
from .models import Member, Batting


class AddMemberForm(forms.Form):
    name = forms.CharField(max_length=40,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': 'Enter member name',
                                      'aria-label': 'Name', 'aria-describedby': 'add-btn'})

                           )
