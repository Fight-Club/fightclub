from django import forms
from django.core.mail import send_mail


class FighterSelectForm(forms.Form):

    def __init__(self, *args, **kwargs):
        choices = kwargs.pop("choices", [])
        super(FighterSelectForm, self).__init__(*args, **kwargs)
        self.fields["who_would_win_in_a_fight_between"] = forms.ChoiceField(
            widget=forms.RadioSelect,
            choices=choices)


class ContactForm(forms.Form):
    Fighter_Name = forms.CharField(max_length=100)
    Description = forms.CharField(widget=forms.Textarea)
    Email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
