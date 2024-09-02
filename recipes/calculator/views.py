from django.shortcuts import render


# Наша база данных рецептов
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

def recipe_view(request, recipe_name):
    recipe = DATA.get(recipe_name)

    if recipe is None:
        context = {'recipe': None}
    else:
        servings = request.GET.get('servings')
        if servings and servings.isdigit():
            servings = int(servings)
        else:
            servings = 1
        updated_recipe = {ingredient: amount * servings for ingredient, amount in recipe.items()}
        context = {'recipe': updated_recipe}

    return render(request, 'index.html', context)
