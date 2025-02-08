from django import forms

class BreachCheckForm(forms.Form):
    email = forms.EmailField(required=False)
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput,
        help_text="We never store passwords"
    )
    phone = forms.CharField(required=False, max_length=20)