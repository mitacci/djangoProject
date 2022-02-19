from django import forms

from djangoProject.app.models import Profile, Note


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'age': 'Age',
            'image_url': 'Link to Profile Image',
        }


class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = "__all__"
        labels = {
            'title': 'Title',
            'content': 'Content',
            'image_url': 'Link to Image',
        }


class EditNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = "__all__"
        labels = {
            'title': 'Title',
            'content': 'Content',
            'image_url': 'Link to Image',
        }


class DeleteNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Note
        fields = "__all__"
        labels = {
            'title': 'Title',
            'content': 'Content',
            'image_url': 'Link to Image',
        }



