from django import forms
from accounts.models import Profile

class ProfileForm(forms.ModelForm):
    telefone = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={'class': 'telefone-mask', 'id': 'telefone'})
    )
    email = forms.EmailField(max_length=254, required=False)

    class Meta:
        model = Profile
        fields = ['telefone']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.user:
            self.fields['email'].initial = self.instance.user.email

    def save(self, commit=True):
        profile = super().save(commit=False)
        profile.user.email = self.cleaned_data['email']
        if commit:
            profile.user.save()
            profile.save()
        return profile
