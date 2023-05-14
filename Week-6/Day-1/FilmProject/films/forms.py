from django import forms
from .models import Film, Director, Comments

class AddFilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = "__all__"
        widgets = {
            "release_date": forms.DateInput(attrs={'type': "date"}),
        }

class AddDirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = "__all__"

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = "__all__"
        labels = {
            'comment': "Let your comment:"
        }
        widgets = {
            'comment': forms.Textarea(),
            'user': forms.HiddenInput(),
            'film': forms.HiddenInput(),
        }