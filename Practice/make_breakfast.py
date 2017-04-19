def make_breakfast(Type):
    """ Make me some breakfast"""
    print("Gather Ingredients")
    print("Categorize the ingredients")
    print("Mix the ingredients")
    print("Heat up the pan")
    print("Pour ingredients into the pan")

    userinput = input("Do you want extra ingredients? Type Y for YES or N for NO: ")
    if userinput == "Y":
        ingredients = []

        def add_ingredient(Ingredient):
            ingredients.append(Ingredient)

        additional_ingredient = input("Enter Additional Ingredients: ")
        add_ingredient(additional_ingredient)

        return "Yummy " + Type + ", ".join(ingredients) 

    elif userinput == "N":
        return "Yummy " + Type + "!"

    else:
        print("Please enter valid input")
    # print("Yummy " + Type + "!")

    

   

print(make_breakfast("Eggs"))