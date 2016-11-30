from django import forms


# Creates a new form with the following field and attributes.
# Each time the class is instantiated it constructs a new html <form>
class NameForm(forms.Form):
    attrs={'placeholder': '########', 'autofocus': 'autofocus', 'class': 'form-control', 'id': 'num'}
    w_number = forms.CharField(widget=forms.TextInput(attrs), label='W   ', label_suffix='', max_length=100)
