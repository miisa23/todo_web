from django.urls import path

from . import views

urlpatterns = [
    # path('', views.home_view, name='home'),
    path('', views.HomeView.as_view(), name='home'),
    path('registration/', views.registration_view, name='registration'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('note/create/', views.create_view, name='create'),

    path('categories/<int:category_id>', views.get_notes_by_category, name='category_notes'),
    path('notes/<int:note_id>', views.note_detail, name='note_detail'),
    path('note/<int:pk>/update/', views.NoteUpdateView.as_view(), name='update'),
    path('note/<int:pk>/delete/', views.NoteDeleteView.as_view(), name='delete'),
    path('note/<int:obj_id>/<str:action>/', views.add_mark_done, name='add_mark_done'),
    path('search/', views.SearchResults.as_view(), name='search')
]