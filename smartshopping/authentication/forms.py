from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label='Username',
                               widget=forms.TextInput(attrs={
                                   'required': 'required'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'required': 'required'}),
                               label='Password')


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30, label='Username',
                               widget=forms.TextInput(
                                   attrs={'required': 'required'}))
    email = forms.CharField(max_length=100, label='Email',
                            widget=forms.EmailInput(attrs=
                                                    {'required': 'required'}))
    password = forms.CharField(max_length=160, label='Password',
                               widget=forms.PasswordInput(
                                   attrs={'required': 'required'}))
    password2 = forms.CharField(max_length=160,
                                label='Retype password',
                                widget=forms.PasswordInput(
                                    attrs={'required': 'required'}))
    address = forms.CharField(max_length=100, label='address',
                               widget=forms.TextInput(
                                   attrs={'required': 'required'}))

    phone = forms.IntegerField(label='Phone number', widget=forms.NumberInput(
        attrs={'required': 'required'}))



class PasswordResetForm(forms.Form):
    oldpass = forms.CharField(max_length=160, min_length=8,
                              label="Old password",
                              widget=forms.PasswordInput(
                                  attrs={'required': 'required'}))
    pass1 = forms.CharField(max_length=160, min_length=8, label="New password",
                            widget=forms.PasswordInput(
                                attrs={'required': 'required'}))
    pass2 = forms.CharField(max_length=160, min_length=8,
                            label="Type again the new password",
                            widget=forms.PasswordInput(
                                attrs={'required': 'required'}))


class ForGotPassword(forms.Form):
    pass1 = forms.CharField(max_length=160, min_length=8, label="New password",
                            widget=forms.PasswordInput(
                                attrs={'required': 'required'}))
    pass2 = forms.CharField(max_length=160, min_length=8,
                            label="Type again the new password",
                            widget=forms.PasswordInput(
                                attrs={'required': 'required'}))

