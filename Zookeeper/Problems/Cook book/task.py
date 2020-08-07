pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

ingredient = input()

if ingredient in pasta:
    print("Pasta time!")

if ingredient in apple_pie:
    print("Apple Pie time!")

if ingredient in ratatouille:
    print("ratatouille time!")

if ingredient in chocolate_cake:
    print("Chocolate Cake time!")

if ingredient in omelette:
    print("Omelette time!")
