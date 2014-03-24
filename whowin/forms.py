from django import forms


class FighterSelectForm(forms.Form):

    def __init__(self, *args, **kwargs):
        choices = kwargs.pop("choices", [])
        super(FighterSelectForm, self).__init__(*args, **kwargs)
        self.fields["who_would_win_in_a_fight_between"] = forms.ChoiceField(
            widget=forms.RadioSelect,
            choices=choices)

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)