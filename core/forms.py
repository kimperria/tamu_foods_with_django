from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Vendor, Merchant
## Dependancy on tamueats
from tamueats.models import Customer


class UserRegistrationForm(UserCreationForm):
    '''
     Class to handle customer registration
    '''

    class Meta:
        model = User
        fields = ('username','email', 'first_name', 'last_name', 'password1', 'password2', 'is_customer')

class NonCustomerRegistrationForm(UserRegistrationForm):
    '''
    Class to handle non customer account registration
    '''

    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2', 'is_vendor', 'is_merchant')

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    password = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'profile_photo']
        exclude = ('currently',)

class UpdateUserProfilePicForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_photo']

class CustomerInformationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['phone_number']

class VendorInformationForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['company_name', 'location', 'company_description']

class MerchantInformationForm(forms.ModelForm):
    class Meta:
        model = Merchant
        fields = ['merchant_name', 'merchant_description']