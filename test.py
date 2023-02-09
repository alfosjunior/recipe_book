
"""
This is a recipe book project using folders instead of databases. 
The idea of this exercise is to practice folder management commands and format functions.
"""
from os import system
import os
import sys

OPTIONS = """
1. reed recipe: 
2. create recipe
3. create category
4. delete recipe
5. delete category
6. close program
"""

def get_content_path(category):
    recipes = os.listdir(f"./recipes{category}")
    return recipes

def control():
    while True:
        escape = input("press 'x' to continue \n")
        if escape.lower() == "x":
            break

def asker(option, values):
    print(f"choose one of the following {option}: ")
    print(', '.join(values))
    answer = input("\n")
    return answer

def create_recipe(category):
    print("insert the name of the new recipe: \n")
    name = input()
    recipe = input(f"insert the new recipe for {name}: \n")
    with open(f"./recipes/{category}/{name}.txt", 'w') as new_recipe:
        new_recipe.write(recipe)

def total_recipes():
    categories = get_content_path('')
    num_categories = len(categories)
    num_recipes = 0
    for category in categories:
        recipes = get_content_path(f"/{category}")
        num_recipes += len(recipes)

    return num_categories, num_recipes

while True:

    try: 
        num_categories, num_recipes = total_recipes()
        system('cls')
        print("Welcome! This is the best recipe book ever!!")
        print(f'current directory is: {os.getcwd()}')
        print(f"total of recipes is: {num_recipes}")
        print("please choose one of the following options")
        print(OPTIONS)
        option = int(input("\n Option is: "))
        categories = get_content_path('')

        if option == 1: 
            category_selected = asker("categories", categories)
            assert category_selected in categories
            
            recipes = get_content_path(f'/{category_selected}')
            recipe_selected = asker("recipes", recipes)
            assert recipe_selected in recipes

            with open(f'./recipes/{category_selected}/{recipe_selected}', "r") as recipe_to_read:
                content = recipe_to_read.read()
            print(content)
            control()
        
        elif option == 2:
            category_selected = asker("categories", categories)
            assert category_selected in categories
            create_recipe(category_selected)
            control()
        
        elif option == 3: 
            category_name = input("please insert the name of the new category: \n")
            os.mkdir(f"./recipes/{category_name}")
            control()
        
        elif option == 4:
            category_selected = asker("categories", categories)
            assert category_selected in categories

            recipes = get_content_path(f'/{category_selected}')
            recipe_selected = asker("recipes", recipes)
            assert recipe_selected in recipes

            while True:
                confirmation = input("do you want continue? Y/N \n")
                if confirmation.lower() == "y":
                    os.remove(f"./recipes/{category_selected}/{recipe_selected}")
                    break
                elif confirmation.lower() == "n":
                    break
            control()


        elif option == 5:
            category_selected = asker("categories", categories)
            assert category_selected in categories

            recipes = get_content_path(f'/{category_selected}')
            for recipe in recipes:
                os.remove(f"./recipes/{category_selected}/{recipe}")

            os.rmdir(f"./recipes/{category_selected}")
            print("recipe has been deleted!")
            control()

        elif option == 6:
            print("thank you to use our recipe program!")
            control()
            break
            
        else:
            print("wrong option. ")
            control()
        

    except AssertionError as ae:
        print("incorrect option")
        control()

    except Exception as e: 
        print("software error ")
        print(e)
        print("---")
        print("Error on line {}".format(sys.exc_info()[-1].tb_lineno))
        control()



            






