def meal_planner():

    nuggets_and_chips = ["Nuggets", "Potatoes", "Oil"]  # Recipes and Ingredients
    salmon_and_salad = ["Salmon", "Pepper", "Lettuce"]
    yummy_bread = ["Bread", "Eggs", "Milk"]
    cereal = ["Cereal", "Milk"]
    toast = ["Bread", "Butter"]
    roast_potatoes = ["Potatoes", "Oil", "Butter"]
    salmon_roast = ["Salmon", "Potatoes", "Oil", "Butter"]
    ingredients_list = ["Nuggets", "Potatoes", "Oil", "Salmon", "Milk", "Pepper", "Lettuce", "Bread", "Eggs",
                        "Cereal", "Butter"]
    total_ingredients = []

    print("Here are a list of ingredients you can add: \n" + str(ingredients_list))  # 1: Get three  ingredients
    first_ingredient = input("Add your first ingredient from the list to plan a meal: ").capitalize()
    correct_counter = 0
    while correct_counter < 1:
        if first_ingredient in ingredients_list:
            correct_counter += 1
            total_ingredients.insert(0, first_ingredient)
        else:
            print("Sorry, that didn't work, please try again")
            first_ingredient = input("Add your first ingredient from the list to plan a meal: ").capitalize()

    print("You have added: " + first_ingredient)

    second_ingredient = input("Add your second ingredient from the list to plan a meal: ").capitalize()
    correct_counter = 0
    while correct_counter < 1:
        if second_ingredient in ingredients_list:
            correct_counter += 1
            total_ingredients.insert(1, second_ingredient)
        else:
            print("Sorry, that didn't work, please try again")
            second_ingredient = input("Add your second ingredient from the list to plan a meal: ").capitalize()

    print("You have added: " + second_ingredient)
    total_ingredients_display = ("Total ingredients: " + first_ingredient + " + " + second_ingredient)
    print(total_ingredients_display)

    third_ingredient = input("Add your third ingredient from the list to plan a meal: ").capitalize()
    correct_counter = 0
    while correct_counter < 1:
        if third_ingredient in ingredients_list:
            correct_counter += 1
            total_ingredients.insert(2, third_ingredient)
        else:
            print("Sorry, that didn't work, please try again")
            third_ingredient = input("Add your third ingredient from the list to plan a meal: ").capitalize()

    print("You have added: " + third_ingredient)
    total_ingredients_display = ("Total ingredients: " + first_ingredient + " + " + second_ingredient + " + " +
                                 third_ingredient)
    print(total_ingredients_display)

    yes_responses = ["Yes", "Y", "Yes", "Yeah", "Yep"]  # Would like to continue?
    add_more_question = input("Would you like to add more ingredients? ").capitalize()
    keep_going = 0
    if add_more_question in yes_responses:
        print("Ok great!")
        while keep_going < 1:
            another_ingredient = input("Add your next ingredient: ").capitalize()
            correct_counter = 0
            while correct_counter < 1:
                if another_ingredient in ingredients_list:
                    total_ingredients.append(another_ingredient)
                    print("You have added: " + another_ingredient)
                    total_ingredients_display = ("Total ingredients: " + first_ingredient + " + " + second_ingredient
                                                 + " + " + third_ingredient + " + " + another_ingredient)
                    print(total_ingredients_display)
                    correct_counter += 1
                    add_more_question = input("Would you like to add more ingredients? ").capitalize()
                    if add_more_question in yes_responses:
                        keep_going = 0
                    else:
                        keep_going += 1
                else:
                    print("Sorry, that didn't work, please try again")
                    another_ingredient = input("Add your next ingredient: ").capitalize()
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


meal_planner()
