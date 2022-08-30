from .models import User
from django import forms
from django.contrib.auth.hashers import make_password
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget

# signup
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "input ",
                "value": "",
                "placeholder": "Password",
            },
        ),
    )
    confirm_password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "input ",
                "value": "",
                "placeholder": "Confirm Password",
            },
        ),
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "gender",
            'blood_group',
            "phone_number",
            "password",
        ]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error("confirm_password", "Password does not match")

        if password == "":
            cleaned_data.pop("password")
            cleaned_data.pop("confirm_password")

        else:
            hashed_password = make_password(password)
            cleaned_data["password"] = hashed_password
            cleaned_data["confirm_password"] = hashed_password

        return cleaned_data


class UserProfileForm(forms.ModelForm):
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "value": "",
                "placeholder": "Password",
                "autocomplete": "new-password",
            },
        ),
    )
    confirm_password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "value": "",
                "placeholder": "Confirm Password",
            },
        ),
    )

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["present_address"].required = False
        self.fields["permanent_address"].required = False

        # Add class
        self.fields["gender"].widget.attrs = {"class": "form-select"}
        self.fields["occupation"].widget.attrs = {"class": "form-select"}

        self.fields['blood_group'].widget.attrs = {"class": "form-select"}

        self.fields["workplace"].widget.attrs.update(
            {
                "placeholder": "Educational Institute"
                if self.instance.occupation == "Student"
                else "Workplace"
            }
        )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error("confirm_password", "Password does not match")

        if password == "":
            cleaned_data.pop("password")
            cleaned_data.pop("confirm_password")

        else:
            hashed_password = make_password(password)
            cleaned_data["password"] = hashed_password
            cleaned_data["confirm_password"] = hashed_password

        return cleaned_data

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "phone_number",
            "password",
            "district",
            "present_address",
            "permanent_address",
            "gender",
            'blood_group',
            "occupation",
            "workplace",
            "age",
            "email",
            "last_blood_donation_date",
        ]

        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "First Name",
                },
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Last Name",
                },
            ),
            "phone_number": PhoneNumberInternationalFallbackWidget(
                attrs={
                    "class": "form-control",
                    "placeholder": "Phone Number",
                },
            ),
            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "District Name",
                },
            ),
            "present_address": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Present Address",
                },
            ),
            "permanent_address": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Permanent Address",
                },
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email Address",
                },
            ),
            "last_blood_donation_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Last Blood Donation Date",
                },
            ),
            "workplace": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "age": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Age",
                }
            ),
        }
