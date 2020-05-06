from django.shortcuts import render

from recipe.models import RecipeItem, Author

# Create your views here.


def index(request):
    data = RecipeItem.objects.all()
    return render(request, 'index.html', {'data': data})


def detail_recipe(request, id):
    data = RecipeItem.objects.filter(id=id).first()
    return render(request, 'recipe.html', {'data': data})


def detail_author(request, id):
    person = Author.objects.get(id=id)
    data = RecipeItem.objects.filter(author=person)
    return render(request, 'author.html', {'author': person, 'data': data})
