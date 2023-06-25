from django.http import HttpResponse
from django.shortcuts import render
import os


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def recipe_view(request, content):
    servings = int(request.GET.get("servings", 1))
    #recipe = request.GET.get('recipe')
    try:
        some_dishes = {}
        recipe = DATA[content]
        for ingredient, amount in recipe.items():
            new_amount = amount * servings
            some_dishes[ingredient] = new_amount
        context = {
            'recipe': some_dishes
            }

    except KeyError:
        context = {
            'recipe': None
        }

    return render(request, 'calculator/index.html', context)


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
