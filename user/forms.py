from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label="Username")
    password = forms.CharField(max_length=10, label="Password", widget=forms.PasswordInput)
    

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30, label="Username")
    password = forms.CharField(max_length=10, label="Password", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=10, label="Confirm password", widget=forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]
        confirm = self.cleaned_data["confirm"]
        
        
        if password and confirm and password != confirm:
            raise forms.ValidationError("Passwords doesn't match!!")
        
        values = {
            "username": username,
            "password": password
        }
        
        return values
