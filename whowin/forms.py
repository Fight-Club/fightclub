from django import forms


class FighterSelectForm(forms.Form):

    def __init__(self, *args, **kwargs):
        choices = kwargs.pop("choices", [])
        super(FighterSelectForm, self).__init__(*args, **kwargs)
        self.fields["who_would_win_in_a_fight_between"] = forms.ChoiceField(
            widget=forms.RadioSelect,
            choices=choices)
