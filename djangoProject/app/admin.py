from django.contrib import admin

from djangoProject.app.models import Profile, Note


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    pass
