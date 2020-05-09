from django.shortcuts import render, reverse, HttpResponseRedirect

from recipe.models import RecipeItem, Author
from recipe.forms import RecipeAddForm

# Create your views here.


def index(request):
    data = RecipeItem.objects.all()
    return render(request, 'index.html', {'data': data})


def recipeadd(request):
    html = "recipeaddform.html"

    if request.method == 'POST':
        form = RecipeAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            RecipeItem.object.Create(
                title=data['title'],
                description=data['description'],
                author=data['author']
            )
            return HttpResponseRedirect(reverse('homepage'))


    form = RecipeAddForm()

    return render(request, html, {"form": form})


def detail_recipe(request, id):
    data = RecipeItem.objects.filter(id=id).first()
    return render(request, 'recipe.html', {'data': data})


def detail_author(request, id):
    person = Author.objects.get(id=id)
    data = RecipeItem.objects.filter(author=person)
    return render(request, 'author.html', {'author': person, 'data': data})
