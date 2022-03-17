def meal_planner():

    yes_responses = ["Yes", "Y", "Yes", "Yeah", "Yep"]
    no_responses = ["No", "N", "Na", "Nope", "No thanks", "No thank you"]

    nuggets_and_chips = ["Nuggets", "Potatoes", "Oil"]  # Recipes and Ingredients
    salmon_and_salad = ["Salmon", "Pepper", "Lettuce"]
    yummy_bread = ["Bread", "Eggs", "Milk"]
    cereal = ["Cereal", "Milk"]
    toast = ["Bread", "Butter"]
    roast_potatoes = ["Potatoes", "Oil", "Butter"]
    salmon_roast = ["Salmon", "Potatoes", "Oil", "Butter"]
    recipe_list = ["Nuggets and Chips", "Salmon with Salad", "Yummy bread", "Cereal", "Toast",
                   "Roast Potatoes", "Salmon Roast"]
    ingredients_list = ["Nuggets", "Potatoes", "Oil", "Salmon", "Milk", "Pepper", "Lettuce", "Bread", "Eggs",
                        "Cereal", "Butter"]
    total_ingredients = []
    new_recipe_input_list = []

    print("Here are the recipes in the system: \n"
          "Nuggets and Chips\n"
          "Salmon with Salad\n"
          "Yummy bread\n"
          "Cereal\n"
          "Toast\n"
          "Roast Potatoes\n"
          "Salmon Roast\n")

    correct = 0
    ultimate_correct = 0
    while correct == 0:
        new_recipe = input("Would you like to add a new recipe?\n").capitalize()
        correct = 0
        if new_recipe in yes_responses:
            while correct == 0:
                new_recipe_input = input("What is the name of your recipe?\n").capitalize()
                while correct == 0:
                    if new_recipe_input in recipe_list:
                        print("Sorry, please try again")
                        new_recipe_input = input("What is the name of your recipe?\n").capitalize()
                    else:
                        correct += 1
                if new_recipe_input not in recipe_list:
                    new_ingredient = input("Add first ingredient for this recipe\n").capitalize()
                    correct = 0
                    while correct == 0:
                        if new_ingredient in ingredients_list:
                            print("Sorry, please try again")
                            new_ingredient = input("Add first ingredient for this recipe\n").capitalize()
                        else:
                            correct += 1
                    if new_ingredient not in ingredients_list:
                        ingredients_list.append(new_ingredient)
                        print("Updated recipe list: \n" + str(ingredients_list))
                        ingredients_list.append(new_ingredient)
                        new_recipe_input_list.append(new_ingredient)
                        new_ingredient2 = input("Add second ingredient for this recipe\n").capitalize()
                        correct = 0
                        while correct == 0:
                            if new_ingredient2 in ingredients_list:
                                print("Sorry, please try again")
                                new_ingredient2 = input("Add second ingredient for this recipe\n").capitalize()
                            else:
                                correct += 1
                        if new_ingredient2 not in ingredients_list:
                            ingredients_list.append(new_ingredient2)
                            print("Updated recipe list: \n" + str(ingredients_list))
                            ingredients_list.append(new_ingredient2)
                            new_recipe_input_list.append(new_ingredient2)
                            another_new_ingredient_question = input("Add another ingredient for recipe?\n").capitalize()
                            if another_new_ingredient_question in yes_responses:
                                repeat_question = 0
                                while repeat_question == 0:
                                    if another_new_ingredient_question in yes_responses:
                                        another_new_ingredient\
                                            = input("Add another ingredient for this recipe\n").capitalize()
                                        if another_new_ingredient in ingredients_list:
                                            print("Sorry, please try again")
                                        else:
                                            ingredients_list.append(another_new_ingredient)
                                            print("Updated recipe list: \n" + str(ingredients_list))
                                            ingredients_list.append(another_new_ingredient)
                                            new_recipe_input_list.append(another_new_ingredient)
                                            another_new_ingredient_question\
                                                = input("Add another ingredient for recipe?\n").capitalize()
                                        if another_new_ingredient_question in yes_responses:
                                            repeat_question = 0
                                        elif another_new_ingredient_question in no_responses:
                                            repeat_question = 1
                                            correct += 1
                                            ultimate_correct += 1
                                        else:
                                            another_new_ingredient_question\
                                                = input("Add another ingredient for recipe?\n").capitalize()
                            elif another_new_ingredient_question in no_responses:
                                correct += 1
                                ultimate_correct += 1
                            else:
                                print("Sorry, please try again")
        elif new_recipe in no_responses:
            correct += 1

        else:
            print("Sorry, please try again")

    print("Brilliant\n")
    print("Here are a list of ingredients you can add: \n" + str(ingredients_list))  # 1: Get three  ingredients
    first_ingredient = input("Add your first ingredient from the list to plan a meal: ").capitalize()
    correct_counter = 0
    while correct_counter < 1:
        if first_ingredient in ingredients_list and first_ingredient not in total_ingredients:
            correct_counter += 1
            total_ingredients.insert(0, first_ingredient)
        else:
            print("Sorry, that didn't work, please try again")
            first_ingredient = input("Add your first ingredient from the list to plan a meal: ").capitalize()

    print("Total: ", end="")
    for x in total_ingredients:
        print(str(x))

    second_ingredient = input("Add your second ingredient from the list to plan a meal: ").capitalize()
    correct_counter = 0
    while correct_counter < 1:
        if second_ingredient in ingredients_list and second_ingredient not in total_ingredients:
            correct_counter += 1
            total_ingredients.insert(1, second_ingredient)
        else:
            print("Sorry, that didn't work, please try again")
            second_ingredient = input("Add your second ingredient from the list to plan a meal: ").capitalize()

    print("You have added: " + second_ingredient)
    print("Total: ", end="")
    for x in total_ingredients:
        print(str(x), end=". ")
    print("")

    third_ingredient = input("Add your third ingredient from the list to plan a meal: ").capitalize()
    correct_counter = 0
    while correct_counter < 1:
        if third_ingredient in ingredients_list:
            correct_counter += 1
            total_ingredients.insert(2, third_ingredient)
        else:
            print("Sorry, that didn't work, please try again")
            third_ingredient = input("Add your third ingredient from the list to plan a meal: ").capitalize()

    print("Total: ", end="")
    for x in total_ingredients:
        print(str(x), end=". ")
    print("")

    keep_going = 0
    while keep_going == 0:
        add_more_question = input("Would you like to add more ingredients? ").capitalize()
        if add_more_question in yes_responses:
            print("Ok great!")
            another_ingredient = input("Add your next ingredient: ").capitalize()
            if another_ingredient in ingredients_list and another_ingredient not in total_ingredients:
                total_ingredients.append(another_ingredient)
                print("You have added: " + another_ingredient)
                print("Total: ", end="")
                for x in total_ingredients:
                    print(str(x), end=". ")
                print("")
            else:
                print("Ingredient not found, please try again")

        elif add_more_question not in no_responses and add_more_question not in yes_responses:
            print("Sorry, that didn't work, please try again")

        elif add_more_question in no_responses:
            keep_going += 1

    print("")
    print("Ok, this is what you can make with your ingredients...\n")  # results
    if all(elem in total_ingredients for elem in nuggets_and_chips):
        print("- Nuggets with Chips")
    if all(elem in total_ingredients for elem in salmon_and_salad):
        print("- Salmon with Salad")
    if all(elem in total_ingredients for elem in yummy_bread):
        print("- Yummy bread")
    if all(elem in total_ingredients for elem in cereal):
        print("- Cereal")
    if all(elem in total_ingredients for elem in toast):
        print("- Toast")
    if all(elem in total_ingredients for elem in roast_potatoes):
        print("- Roast Potatoes")
    if all(elem in total_ingredients for elem in salmon_roast):
        print("- Salmon Roast")
    if all(elem in total_ingredients for elem in new_recipe_input_list):
        print("- Salmon Roast")


meal_planner()
