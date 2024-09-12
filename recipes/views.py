from django.shortcuts import render

def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Vanthuir Maia',
    })

def recipe(request, id):
    return render(request, 'recipes/pages/project-view.html', context={
        'name': 'Vanthuir Maia',
    })
