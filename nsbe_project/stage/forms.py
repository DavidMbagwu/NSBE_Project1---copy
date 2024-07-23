from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Member
from . import choices


def pretty_name(field_name):
    return " ".join(
        part.capitalize() for part in field_name.split("_") if part.isalpha()
    )


class MemberSignUpForm(UserCreationForm):
    class Meta:
        model = Member
        fields = [
            "first_name",
            "last_name",
            "mcneese_id",
            "email",
            "linkedin",
            "major",
            "class_standing",
            "nationality",
            "race",
            "gender",
            "password1",
            "password2",
        ]

    class_standing = forms.ChoiceField(
        choices=choices.CLASS_STANDING_CHOICES,
        widget=forms.Select(attrs={"class": "dropdown"}),
    )
    race = forms.ChoiceField(
        choices=choices.RACE_CHOICES, widget=forms.Select(attrs={"class": "dropdown"})
    )
    gender = forms.ChoiceField(
        choices=choices.GENDER_CHOICES, widget=forms.Select(attrs={"class": "dropdown"})
    )
    nationality = forms.ChoiceField(
        choices=choices.COUNTRY_CHOICES,
        widget=forms.Select(attrs={"class": "dropdown"}),
    )
    major = forms.ChoiceField(
        choices=choices.MAJOR_CHOICES, widget=forms.Select(attrs={"class": "dropdown"})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Loop through all fields and remove labels and update the placeholders
        for fieldname, field in self.fields.items():
            # Make every field required
            field.required = True

            # Capitalize labels and add asterisk
            field.label = pretty_name(fieldname)

            field.label_suffix = "*"

            # Add placeholder
            field.widget.attrs["placeholder"] = ""

            # Remove password help text
            field.help_text = None

            # Remove initial value if it was set before
            if isinstance(field, forms.ChoiceField):
                field.choices = [("", "Select")] + list(field.choices)

        self.fields["mcneese_id"].label = "McNeese ID"
        self.fields["password1"].label = "Password"
        self.fields["password2"].label = "Confirm Password"
