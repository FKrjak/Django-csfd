from django import forms


class MovieForm(forms.Form):
    input = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"placeholder": "input...", "onchange": "submit();"}
        ),
    )
