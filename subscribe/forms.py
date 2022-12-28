from django import forms
from .models import Subscribe
from django.utils.translation import gettext_lazy as _

# Below is the code for the model forms

class SubscribeForm(forms.ModelForm):
    class Meta:
        model=Subscribe
        fields = '__all__'
        #  to customize the label, error_messages we can use below one 
        labels = {
            'first_name':_('Enter first name'),
            'last_name':_('Enter last name'),
            'email':_('Enter Email')       
        }
        # help_texts = {'first_name': _('Enter Characters only')}
        error_messages ={
            
            'first_name': {
                'required':_('You cannont move without your first name')
            }
        }
         
        # fields = ['first_name','last_name','email'] 
        # exclude = ('first_name') just add this code at the top if you want to remove one specified field 
        # fields can be __all__ of manually we can assign to a list and pick up the models that you want to convert 
        


# These validators are used to validate the data is entered properly by the user or not
# def validate_comma(value):
#     if ',' in value:
#         raise forms.ValidationError("Invalid")
#     return value

# class SubscribeForm(forms.ModelForm):
#     first_name = forms.CharField(max_length=100,required = False, label = "Enter your first name", validators=[validate_comma])
#     last_name = forms.CharField(max_length=100)
#     email = forms.EmailField(max_length=100, validators = [validate_comma])
    
    
    # This is also similar function to validate_comma both the functions in the above does the same thing   
    # def clean_first_name(self):
    #     data = self.cleaned_data['first_name']
    #     if "," in data:
    #         raise forms.ValidationError("Invalid First Name")
    #     return data