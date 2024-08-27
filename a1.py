"""
CSSE1001 Assignment 1
Semester 1, 2023
"""

# Fill these in with your details
__author__ = "Ryu Otsu"
__email__ = "s4800316@uqconnect.edu.au"
__date__ = "03/03/2023"

from constants import *


def num_hours() -> float:
    """
    Return hours spent on the assignment.

    >>> num_hours()
        30
    
    """
    print(30)
    
def get_recipe_name(recipe: tuple[str, str]) -> str:
    """
    Returns the name of the recipe.

    Parameters:
        recipe(tuple[str, str]): Recipe used to find the recipe name.

    Return:
        str: Recipe name

    >>> get_recipe_name(('chocolate peanut butter banana shake',
            '1 large banana,240 ml almond milk'))
        'chocolate peanut butter banana shake'
    """
    reci, ingredient = recipe
    return reci

def parse_ingredient(raw_ingredient_detail: str) -> tuple[float, str, str]:
    """
    Return the ingredient breakdown from the details amount, measure, and ingredient.

    Parameters:
        raw_ingredient_detail(str): An ingredient detail that will get broken down.

    Return:
        tuple[float, str, str]: Ingredient detail.

    >>> parse_ingredient('0.5 tsp coffee granules')
        (0.5, 'tsp', 'coffee granules')
    """
    amount, measure, ingredient = raw_ingredient_detail.split(' ', 2)
    return(float(amount), measure, ingredient)

def create_recipe() -> tuple[str, str]:
    """
    Returns a recipe after recipe name and ingredient are entered.

    Parameters:
        None

    Return:
        tuple[str, str]: Recipe detail.

    >>> create_recipe()
        Please enter the recipe name: peanut butter
        Please enter an ingredient: 300 g peanuts
        Please enter an ingredient: 0.5 tsp salt
        Please enter an ingredient: 2 tsp oil
        Please enter an ingredient:
        ('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil')
    """

    count = 0
    ingredient = ""
    
    while count == 0:
        recipe_name = input("Please enter the recipe name: ")
        count += 1
        while count == 1:
            ingredient_name = input("Please enter an ingredient: ")
            ingredient = ingredient_name
            count += 1
            while ingredient_name != "":
                ingredient_name = input("Please enter an ingredient: ")
                if ingredient_name == "":
                    break
                else:
                    ingredient = ingredient + "," + ingredient_name
    return(recipe_name, ingredient)

def recipe_ingredients(recipe: tuple[str,str]) -> tuple[tuple[float, str, str]]:
    """
    Returns the ingredients of a recipe amount, measure, and ingredient.

    Parameters:
        recipe(tuple[str, str]): Recipe used to obtain ingredient details.

    Return:
        tuple[tuple[float, str, str]]: Tuples of ingredient details.

    >>> recipe_ingredients(('peanut butter',
            '300 g peanuts,0.5 tsp salt,2 tsp oil'))
        ((300.0, 'g', 'peanuts'), (0.5, 'tsp', 'salt'), (2.0, 'tsp', 'oil'))
    """

    recipe_name, ingredient = recipe
    ingredient = ingredient.split(",")
    ingredients = []


    for ingredient_detail in ingredient:
        amount, measure, ingredient = ingredient_detail.split(" ", 2)
        ingredients.append((float(amount), measure, ingredient))
    return tuple(ingredients)


def add_recipe(new_recipe: tuple[str, str], recipes: list[tuple[str, str]]) -> None:
    """
    Add a given recipe into the list of recipes.

    Parameters:
        new_recipe(tuple[str, str]): Recipe that will be added to the recipe list.
        recipes(list[tuple[str, str]]): List of recipes.

    Return:
        list[tuple[str, str]]: List of recipes.
        
    >>> recipes = []
    >>> recipe = ('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil')
    >>> add_recipe(recipe, recipes)
    >>> recipes
        [('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil')]
    """
    recipes.append(new_recipe)

def find_recipe(recipe_name: str, recipes: list[tuple[str, str]]) -> tuple[str, str] | None:
    """
    Return a recipe if the given recipe name is in the list of recipes, or none if the given recipe name is not in the list of recipes.

    Parameters:
        recipe_name(str): A recipe name that wants to be found.
        recipes(list[tuple[str, str]]): List of recipes.

    Return:
        tuple[str, str]: Recipe name and ingredients
        None: Recipe not in the list

    >>> recipes = [('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil')]
    >>> find_recipe('peanut butter', recipes)
        ('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil')
    >>> find_recipe('cinnamon rolls', recipes)
    >>> print(find_recipe('cinnamon rolls', recipes))
        None
    """

    for recipe in recipes:
        if recipe[0] == recipe_name:
            return(recipe)
    return None

def remove_recipe(name: str, recipes: list[tuple[str, str]]) -> None:
    """
    Remove a recipe from the list of recipes given the name of a recipe.
    Nothing happens if the recipe name does not match any of the recipes within the list of recipes.

    Parameters:
        name(str): Name of the recipe
        recipes(list[tuple[str, str]]): List of recipes.

    Return:
        None.

    >>> recipes = [('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil'),
            ('cinnamon rolls', '480 ml almond milk,115 g Nuttelex,50 g sugar,7 g
            active dry yeast,5.5 cup flour,1 tsp salt,170 g Nuttelex,165 g brown
            sugar,2 tbsp cinnamon,160 g powdered sugar,30 ml almond milk,0.5 tsp
            vanilla extract')]
    >>> remove_recipe('cinnamon rolls', recipes)
    >>> recipes
        [('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil')]
    """
    for recipe in recipes:
        if recipe[0] == name:
            recipes.remove(recipe)

def get_ingredient_amount(ingredient: str, recipe: tuple[str, str]) -> tuple[float, str] | None:
    """
    Return the amount and measure of a certain ingredient, given the ingredient name as a str and a recipe.

    Parameters:
        ingredient(str): An ingredient name used to find the amount measure of the ingredient.
        recipe(tuple[str, str]): Recipe.

    Return:
        tuple[str, str]: The amount and measure of a n ingredient.

    >>> recipe = ('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil')
    >>> get_ingredient_amount('peanuts', recipe)
        (300.0, 'g')
    >>> get_ingredient_amount('soy beans', recipe)
    
    """    

    reci, ingre = recipe
    ingre = ingre.split(",")
    ingredients = []


    for ingredient_detail in ingre:
        single_ingredient = ingredient_detail.split(" ", 2)
        ingredients.append(single_ingredient)
        for single_ingredient in ingredients:
            if single_ingredient[2] == ingredient:
                return float(single_ingredient[0]), single_ingredient[1]
        return None

def add_to_shopping_list(ingredient_detail: tuple[float, str, str],
    shopping_list: list[tuple[float, str, str] | None]) -> None:
    """
    Add an ingredient to the shopping list.
    If the ingredient already exists within the shopping list then the amount should be combined.

    Parameters:
        ingredient_detail(tuple[float, str, str]): An ingredient that will be added to the shopping list.
        shopping_list(list[tuple[float, str, str]): Shopping list.

    Return:
        None.
        
    >>> shopping_list = [(300.0, 'g', 'peanuts')]
    >>> add_to_shopping_list((1000.0, 'g', 'tofu'), shopping_list)
    >>> shopping_list
        [(300.0, 'g', 'peanuts'), (1000.0, 'g', 'tofu')]
    >>> add_to_shopping_list((1200.0, 'g', 'peanuts'), shopping_list)
    >>> shopping_list
        [(1500.0, 'g', 'peanuts'), (1000.0, 'g', 'tofu')]
    """

    for ingredients in shopping_list:
        amount, measure, ingredient = ingredients
        amount_1, measure_1, ingredient_1 = ingredient_detail
        if ingredient == ingredient_1:
            updated_ingredient = ((amount + amount_1), measure, ingredient)
            shopping_list.remove(ingredients)
            shopping_list.append(updated_ingredient)
            break
        elif ingredients == shopping_list[-1]:
            shopping_list.append(ingredient_detail)
            break

def remove_from_shopping_list(ingredient_name: str, amount: float, shopping_list: list) -> None:
    """
    Remove a certain amount of an ingredient, with the given ingredient_name, from the shopping_list.
    The ingredient will be removed if the amount goes below 0.

    Parameters:
        ingredient_name(str): An ingredient that wants to be removed.
        amount(float): A certain amount that wants to be removed.
        shopping_list(list): Shopping list.

    >>> shopping_list = [(1500.0, 'g', 'peanuts'), (0.5, 'tsp', 'salt')]
    >>> remove_from_shopping_list(0.2, 'tsp', 'salt')
    >>> shopping_list
        [(1500.0, 'g', 'peanuts'), (0.3, 'tsp', 'salt'),]
    >>> remove_from_shopping_list(0.5, 'tsp', 'salt')
    >>> shopping_list
        [(1500.0, 'g', 'peanuts')]
    """

    for each_ingredient in shopping_list:
        amount_1, measure, ingredient = each_ingredient
        if ingredient == ingredient_name:
            updated_ingredient = ((amount_1 - amount), measure, ingredient)
            if (amount_1 - amount) > 0:
                shopping_list.remove(each_ingredient)
                shopping_list.append(updated_ingredient)
                break
            else:
                shopping_list.remove(each_ingredient)
                break

def generate_shopping_list(recipes: list[tuple[str, str]]) -> list[tuple[float, str, str]]:
    """
    Return a list of ingredients, (amount, measure, ingredient_name), given a list of recipes.

    Parameters:
        recipes(list[tuple[str, str]]): List of recipes used to find out the required ingredients.

    Return:
        list[tuple[float, str, str]]): List of required ingredients.

    >>> shopping_list = generate_shopping_list([PEANUT_BUTTER,
            MUNG_BEAN_OMELETTE])
    >>> shopping_list
        [(300.0, 'g', 'peanuts'), (1.0, 'tsp', 'salt'), (3.0, 'tsp', 'oil'),
        (1.0, 'cup', 'mung bean'), (0.75, 'tsp', 'pink salt'), (0.25, 'tsp',
        'garlic powder'), (0.25, 'tsp', 'onion powder'), (0.125, 'tsp',
        'pepper'), (0.25, 'tsp', 'turmeric'), (1.0, 'cup', 'soy milk')]
    """
    
    count = 0
    list_of_recipes = []
    

    for recipe in recipes:
        if count == 1:
            ingredient = recipe[1].split(",")
            for the_ingredient in ingredient:
                amount, measure, ingredient = the_ingredient.split(" ", 2)
                for each_recipe in list_of_recipes:
                    amount_1, measure_1, ingredient_1 = each_recipe
                    if ingredient == ingredient_1:
                        list_of_recipes.append(((float(amount) + amount_1), measure, ingredient))
                        list_of_recipes.remove(each_recipe)
                        break
                    elif each_recipe == list_of_recipes[-1]:
                        list_of_recipes.append((float(amount), measure, ingredient))
                        break
                    
        while count == 0:
            if recipe == recipes[0]:
                ingredient = recipe[1].split(",")
                count += 1
                for the_ingredient in ingredient:
                    amount, measure, ingredient = the_ingredient.split(" ", 2)
                    list_of_recipes.append((float(amount), measure, ingredient))
                

    return list_of_recipes

def display_ingredients(shopping_list: list[tuple[float, str, str]]) -> None:
    """
    Print the given shopping list. Amount right aligned, measure centered, and ingredients left aligned.

    Parameters:
        shopping_list(list[tuple[float, str, str]]): Shopping list that will be displayed.

    Return:
        None.

    >>> display_ingredients([(10.0, 'large', 'banana'), (0.5, 'cup', 'ice'),])
    | 10.0 | large | banana |
    |  0.5 |  cup  | ice    |
    """

    amount_space = 0
    measure_space = 0
    ingredient_space = 0
    
    for ingredient_info in shopping_list:
        amount, measure, ingredient = ingredient_info
        if len(str(amount)) > amount_space:
            amount_space = len(str(amount))

    for ingredient_info in shopping_list:
        amount, measure, ingredient = ingredient_info
        if len(measure) > measure_space:
            measure_space = len(measure)

    for ingredient_info in shopping_list:
        amount, measure, ingredient = ingredient_info
        if len(ingredient) > ingredient_space:
            ingredient_space = len(ingredient)

    if measure_space % 2 != 0:
        for x in shopping_list:
            amount, measure, ingredient = x
            if len(measure) % 2 == 0:
                print("|" + str(amount).rjust(amount_space + 1) + " |" + measure.center(measure_space + 2) + " | " + ingredient.ljust(ingredient_space +1) + " |")
            else:
                print("|" + str(amount).rjust(amount_space + 1) + " |" + measure.center(measure_space + 2) + "| " + ingredient.ljust(ingredient_space +1) + " |")
    else:
        for x in shopping_list:
            amount, measure, ingredient = x
            if len(measure) % 2 == 0:
                print("|" + str(amount).rjust(amount_space + 1) + " |" + measure.center(measure_space + 2) + " | " + ingredient.ljust(ingredient_space +1) + " |")
            else:
                print("|" + str(amount).rjust(amount_space + 1) + " | " + measure.center(measure_space + 2) + "| " + ingredient.ljust(ingredient_space +1) + " |")

def sanitise_command(command: str) -> str:
    """
    Return a standadised command to all lower-case and remove numbers and unnecessary spaces from the string.

    Parameters:
        command(str): A command that will be sanitised.

    Return:
        str: sanitised command.

    >>> sanitise_command('add chocolate Brownies   5')
        'add chocolate brownies'
    """
    word = ""
    
    for character in command:
        if ord(character) in range(ord("A"), ord("Z")):
            word += character.lower()
        elif ord(character) in range(ord("a"), ord("z")) or (character == " " and character != word[-1]):
            word += character
        else:
            pass

    if word[-1] == " ":
        return word[0:-1]
    else:
        return word

def main():
    """
    A command will be prompted.

    Return:
        Returns an output based on the command.
    
    >>> Please enter a command: h
            H or h: Help
            mkrec: creates a recipe, add to cook book.
            add {recipe}: adds a recipe to the collection.
            rm {recipe}: removes a recipe from the collection.
            rm -i {ingredient_name} {amount}: removes ingredient from shopping list. ls: list all recipes in shopping cart.
            ls -a: list all available recipes in cook book.
            ls -s: display shopping list.
            g or G: generates a shopping list.
            Q or q: Quit.
    """
    # cook book
    
    recipe_collection = [
        CHOCOLATE_PEANUT_BUTTER_SHAKE, 
        BROWNIE, 
        SEITAN, 
        CINNAMON_ROLLS, 
        PEANUT_BUTTER, 
        MUNG_BEAN_OMELETTE
    ]
    
    command = 0
    list_of_recipes = []
    list_of_ingredients = []
    shopping_list = []
    
    while command != "q" or command != "Q":
        command = input("Please enter a command: ")
        if command == "h" or command == "H" or command == "":
            print(HELP_TEXT)
        elif command == "ls -a":
            for recipe in recipe_collection:
                print(get_recipe_name(recipe))
        elif command[0:3] == "add":
            recipe_names = []
            for recipe in recipe_collection:
                recipe_name, ingredients = recipe
                recipe_names.append(recipe_name)
            if sanitise_command(command[4:]) in recipe_names:   ## command[4:] is the name of recipe.
                for recipe in recipe_collection:
                    recipe_name, ingredients = recipe
                    if sanitise_command(command[4:]) == recipe_name:
                        list_of_recipes.append(recipe)
            elif sanitise_command(command[4:]) not in recipe_names:
                print("")
                print("Recipe does not exist in the cook book. ")
                print("Use the mkrec command to create a new recipe.")
                print("")
        elif command == "ls":
            if list_of_recipes == []:
                print("No recipe in meal plan yet.")
            else:
                print(list_of_recipes)
        elif command == "ls -s":
            display_ingredients(shopping_list)
        elif command == "g" or command == "G":
            shopping_list = generate_shopping_list(list_of_recipes)
            display_ingredients(shopping_list)
        elif command[:5] == "rm -i":
            ingredient = (len(command) - (len(command.split()[-1]) + 1))    ## ingredient is the length of ingredient name.
                                                                            ## len(command.split()[-1]) + 1) is the length of amount.
            remove_from_shopping_list(command[6:ingredient], float(command.split()[-1]), shopping_list)     
        elif command[:2] == "rm":
            for recipe in list_of_recipes:
                if command[3:] == recipe[0]:    ## command[3:] is the recipe name.
                    list_of_recipes.remove(recipe)
                    break
        elif command == "mkrec":
            new_recipe = create_recipe()
            recipe_collection.append(new_recipe)
        elif command == "q" or command == "Q":
            break    

if __name__ == "__main__":
    main()


