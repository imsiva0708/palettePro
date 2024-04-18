from gemini import getRecipe
from googlesearch import search
from scrap import extract_main_image

def dictionaryMaker(mainlist):
    list_of_dictionaries = []

    for item in mainlist:
        dictionary = {
            'link': item[0],
            'title': item[1],
            'img': item[2]
        }
        list_of_dictionaries.append(dictionary)
    return list_of_dictionaries


def dictionarify(ingredientsList):
    recipeList = getRecipe(ingredientsList)
    twoDlist = []
    for item in recipeList:
        twoDlist.append(search(item))
    return dictionaryMaker(twoDlist)


# dictionarify(['apple','beetroot','grape'])









# [{'link': 'https://www.indianhealthyrecipes.com/palak-paneer-recipe-easy-paneer-recipes-step-by-step-pics/', 'title': "Palak Paneer Recipe (Indian Spinach Paneer) - Swasthi's Recipes", 'img': 'https://www.indianhealthyrecipes.com/wp-content/uploads/2021/06/palak-paneer.jpg.webp'}, {'link': 'https://www.indianhealthyrecipes.com/dosa-recipe-dosa-batter/', 'title': "Dosa Recipe, How to Make Dosa Batter - Swasthi's Recipes", 'img': 'https://www.indianhealthyrecipes.com/wp-content/uploads/2020/07/dosa-recipe.jpg.webp'}, {'link': 'https://www.indianhealthyrecipes.com/soft-idli-recipe-using-idli-rava/', 'title': "Idli Recipe (Idli Batter Recipe with Pro Tips) - Swasthi's Recipes", 'img': 'https://www.indianhealthyrecipes.com/wp-content/uploads/2021/06/idli.jpg.webp'}]