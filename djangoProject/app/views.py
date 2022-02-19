from django.shortcuts import render, redirect

from djangoProject.app.forms import CreateProfileForm, CreateNoteForm, EditNoteForm, DeleteNoteForm
from djangoProject.app.models import Profile, Note


def home(request):
    profile = Profile.objects.first()
    notes = Note.objects.all()
    if not profile:
        return redirect('create profile')
    context = {
        'profile': profile,
        'notes': notes,
    }
    return render(request, 'home-with-profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)


def show_profile(request):
    profile = Profile.objects.first()
    notes = Note.objects.all().count()
    context = {
        'profile': profile,
        'notes': notes,
    }
    return render(request, 'profile.html', context)


def delete_profile(request):
    Note.objects.all().delete()
    Profile.objects.all().delete()

    return redirect('index')


def add_note(request):
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateNoteForm()

    context = {
        'form': form
    }
    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    instance = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditNoteForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditNoteForm(instance=instance)

    context = {
        'pk': instance,
        'form': form,
    }
    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    instance = Note.objects.get(pk=pk)

    if request.method == 'POST':
        form = DeleteNoteForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteNoteForm(instance=instance)

    context = {
        'pk': instance,
        'form': form,
    }
    return render(request, 'note-delete.html', context)


def note_details(request, pk):
    context = {
        'notes': Note.objects.get(pk=pk),
    }
    return render(request, 'note-details.html', context)
