import csv
def read_recipes(file_name):
    list = []
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            dish_name = row[0]
            ingredients = row[5]
            list.append((dish_name, ingredients))
    return list

def search_recipes(list, user_input):
    matching_recipes = []
    for dish_name, ingredients in list:
        if all(ingredient.lower() in user_input for ingredient in ingredients):
            matching_recipes.append(dish_name)
    return matching_recipes

def main():
    file_name = 'test.csv' 
    recipes = read_recipes(file_name)

if __name__ == "__main__":
    main()




























#import os
#
#file = open('test.csv', newline='', mode='r', encoding='utf-8', errors='ignore')
#reader = csv.reader(file)
#
#list = []
#
#try:
# 
#    while True:
#        list.append(str(input("Enter: ")))
#except:
#    print(list)
#
#
#for row in reader:
#    dish_name = row[1]
#    ingredients = row[5]
#    
#    ingredient_list = ingredients.split(',')
#    
#    result = all(item in ingredient_list for item in list)
#    print(ingredient_list)  
#for row in reader:
#    dish_name = row[1]
#    ingredients = row[5]
#    
#    ingredient_list = ingredients.split(',')
#        
#        # Check if the user inputted MAIN INGREDIENT is in the list of ingredients
#    main_ingredient = "chicken"
#
#    for ingredient in ingredient_list:
#        if main_ingredient in ingredient:
#            print(dish_name)