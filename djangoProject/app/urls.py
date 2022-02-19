from django.urls import path

from djangoProject.app.views import home, \
    add_note, edit_note, delete_note, note_details, \
    show_profile, create_profile, delete_profile

urlpatterns = [
    path('', home, name='index'),
    path('add/', add_note, name='add note'),
    path('edit/<int:pk>/', edit_note, name='edit note'),
    path('delete/<int:pk>/', delete_note, name='delete note'),
    path('details/<int:pk>/', note_details, name='note details'),
    path('profile/', show_profile, name='show profile'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/delete/', delete_profile, name='delete profile')


]