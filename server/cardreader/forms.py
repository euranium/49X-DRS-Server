from django import forms


class NameForm(forms.Form):
    w_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'W########', 'autofocus': 'autofocus'}), label='W#   ', max_length=100)

