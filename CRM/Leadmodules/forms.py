from django import forms
from .models import Leadmodule
from django.core.exceptions import ValidationError

class Leadmoduleform(forms.ModelForm):

    class meta:
          
        model=Leadmodule
        fields="__all__"
    
    def clean_user_name(self):
         
        user_name=self.cleaned_data.get("user_name")
        if user_name and user_name[0].islower():
            raise ValidationError("First letter must be uppercase.")
        return user_name
    
    def clean_name(self):

        password=self.cleaned_data.get("password")
        if password and len(password)<4:
            raise ValidationError("password must contain four characters.")
        return password