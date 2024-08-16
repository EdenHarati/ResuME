# forms.py
from django import forms
from .models import UploadedFile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import os
from django.conf import settings

class UploadCVFileForm(forms.ModelForm):
    use_existing_cv = forms.BooleanField(required=False, label="Use an existing CV")
    existing_cv = forms.ModelChoiceField(
        queryset=UploadedFile.objects.none(),
        required=False,
        label="Select an existing CV",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = UploadedFile
        fields = ['file']

    def __init__(self, *args, **kwargs):
        # Extract the user from kwargs and remove it
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        if user:
               # Filter queryset based on the user and ensure the file exists in the folder
            self.fields['existing_cv'].queryset = UploadedFile.objects.filter(
                user=user, file_type='CV'
            ).filter(
                file__isnull=False  # Ensure there's a valid file
            ).filter(
                # Check if the file actually exists in the directory
                file__in=[
                    f"uploads/{file_name}" for file_name in os.listdir(os.path.join(settings.MEDIA_ROOT, 'uploads'))
                ]
            )
            
            # Customize the label to display the file name
            self.fields['existing_cv'].label_from_instance = lambda obj: obj.file.name.split('/')[-1]

        # Make the file field optional
        self.fields['file'].required = False

    def clean(self):
        cleaned_data = super().clean()
        use_existing_cv = cleaned_data.get('use_existing_cv')
        file = cleaned_data.get('file')
        existing_cv = cleaned_data.get('existing_cv')

        # Validate the selection logic
        if not use_existing_cv and not file:
            raise forms.ValidationError("You must either upload a file or choose an existing one.")
        
        if use_existing_cv and not existing_cv:
            raise forms.ValidationError("You selected 'Use an existing CV' but did not choose any file.")
        
        return cleaned_data

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']
# myapp/forms.py

from django.contrib.auth.forms import AuthenticationForm

# myapp/forms.py



class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))



