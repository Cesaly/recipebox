from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User

from recipe.models import RecipeItem, Author
from recipe.forms import RecipeAddForm, AuthorAddForm, LoginForm

# Create your views here.


def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'],
                                password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', '/'))
    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


def index(request):
    data = RecipeItem.objects.all()
    return render(request, 'index.html', {'data': data})


@login_required
def recipeadd(request):
    html = "generic_form.html"

    if request.method == 'POST':
        form = RecipeAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            RecipeItem.objects.create(
                title=data['title'],
                description=data['description'],
                author=data['author']
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = RecipeAddForm()

    return render(request, html, {"form": form})


@staff_member_required
def authoradd(request):
    html = "generic_form.html"

    if request.method == 'POST':
        form = AuthorAddForm(request.POST)
        new_author = form.save(commit=False)
        new_user = User.objects.create_user(
                username=new_author.name,
                password='welcome1',
            )
        new_author.user = new_user
        new_author.save()
        return HttpResponseRedirect(reverse('homepage'))

    form = AuthorAddForm()

    return render(request, html, {'form': form})


def detail_recipe(request, id):
    data = RecipeItem.objects.filter(id=id).first()
    return render(request, 'recipe.html', {'data': data})


def detail_author(request, id):
    person = Author.objects.get(id=id)
    data = RecipeItem.objects.filter(author=person)
    return render(request, 'author.html', {'author': person, 'data': data})
