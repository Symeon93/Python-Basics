toppings = ['pepperoni', 'pineapple',
            'cheese', 'sausage',
            'olives','anchovies',
            'mushrooms']

prices = [2, 6, 1, 3, 2, 7, 2]

num_pizzas = len(toppings)

print("We sell {} different kinds of pizza".format(num_pizzas))

pizzas = list(zip(prices, toppings))

print(pizzas)

pizzas.sort()  # for a list of list sort() compares again the first element which in this case is the price

print(pizzas)

cheapest_pizza = pizzas[0][1]

print(cheapest_pizza)


priciest_pizza = pizzas[-1][1]

print(priciest_pizza)

'''print the first three eleement, in 
this case the three cheapest pizzas'''

three_cheapest = pizzas[:3]

print(three_cheapest)

# measure appearance in a list
num_two_dollar_slices = prices.count(2)

print(num_two_dollar_slices)










