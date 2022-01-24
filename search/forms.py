from django import forms


class searchForm(forms.Form):
    url = forms.URLField(
        label='Website URL:',
        max_length=500,
        widget=forms.URLInput(
            attrs={
                'class':'md-form',
            }
        ),
    )

class saveForm(forms.Form):
     url = forms.URLField(
        widget=forms.HiddenInput(),
     )
     comment = forms.CharField(
        widget=forms.HiddenInput(),
     )

