from django import forms
from models import Fighter


class FighterSelectForm(forms.Form):
    def __init__(self, *args, **kwargs):
        choices = kwargs.pop("choices", [])
        super(FighterSelectForm, self).__init__(*args, **kwargs)
        self.fields["fighter_choices"] = forms.ChoiceField(
            widget=forms.RadioSelect,
            choices=choices)