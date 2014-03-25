from django import forms
from django.conf import settings
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

    def send_email(self):
        cleaned_data = super(ContactForm, self).clean()
        subject = 'Hello'  # cleaned_data.get("Fighter_Name")
        message = 'asdf'  # cleaned_data.get("Description")
        user_email = cleaned_data.get("Email")
        from_email = settings.EMAIL_HOST_USER
        to_list = [user_email, settings.EMAIL_HOST_USER]

        send_mail(subject, message, from_email, to_list, fail_silently=False)
        pass
