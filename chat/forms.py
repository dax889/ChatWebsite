from django import forms
from .models import CustomUser
from .models import Message

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'confirm_password', 'profile_photo']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password") != cleaned_data.get("confirm_password"):
            raise forms.ValidationError("Passwords do not match.")
        
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text', 'image']
        widgets = {
            'text': forms.TextInput(attrs={
                'placeholder': 'Type a message...',
                'class': 'chat-text-input',
                'id': 'chat-text-input'
            }),
            'image': forms.ClearableFileInput(attrs={
                'id': 'id_image'
            }),
        }
