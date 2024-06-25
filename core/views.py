from django.shortcuts import render, redirect
from .models import Note, Category, Done
from .forms import LoginForm, RegistrationForm, NoteForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import UpdateView, DeleteView, ListView
from django.db.models import Q


# def home_view(request):
#     notes = Note.objects.all()
#
#     # categories = Category.objects.all()
#     context = {
#         'notes': notes,
#         # 'categories': categories
#     }
#     return render(request, 'core/index.html', context)


class HomeView(ListView):
    template_name = 'core/index.html'
    context_object_name = 'notes'
    model = Note


def get_notes_by_category(request, category_id):
    notes = Note.objects.filter(category__id=category_id)
    context = {
        'notes': notes
    }
    return render(request, 'core/index.html', context)


def note_detail(request, note_id):
    note = Note.objects.get(pk=note_id)
    context = {
        'note': note
    }

    return render(request, 'core/detail.html', context)


def registration_view(request):
    if request.method == 'POST':
        print(request.POST)
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'core/registration.html', context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'core/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('home')


def create_view(request):
    if request.method == 'POST':
        form = NoteForm(data=request.POST, files=request.FILES)
        if form.is_valid():
           form = form.save(commit=False)
           form.author = request.user
           form.save()
           return redirect('note_detail', form.pk)
    else:
        form = NoteForm()
    context = {
        'form': form
    }
    return render(request, 'core/create.html', context)


class NoteUpdateView(UpdateView):
    model = Note
    template_name = 'core/create.html'
    form_class = NoteForm


class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'core/note_confirm_delete.html'
    success_url = '/'


def add_mark_done(request, obj_id, action):
    from django.shortcuts import get_object_or_404

    obj = get_object_or_404(Note, pk=obj_id)

    try:
        obj.done
    except Exception as e:
        Done.objects.create(note=obj)

    if action == 'done':
        obj.done.user.add(request.user.pk)

    return redirect(request.environ['HTTP_REFERER'])


class SearchResults(HomeView):
    def get_queryset(self):
        print(self.request.GET)
        query = self.request.GET.get('q')
        return Note.objects.filter(
            Q(title__iregex=query) | Q(text__iregex=query)
        )