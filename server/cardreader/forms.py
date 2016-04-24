from django import forms


# Creates a new form with the following field and attributes.
# Each time the class is instantiated it constructs a new html <form>
class NameForm(forms.Form):
    w_number = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '########', 'autofocus': 'autofocus'}), label='W   ', max_length=100)

