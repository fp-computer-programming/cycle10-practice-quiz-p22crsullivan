# Author: CRS 01/27/22
# Question 1
from operator import index


def food_costs(groceries, costs):
# Create for loop to enumerate the lists
    for items in groceries:
        for index, value in enumerate(items):
            groceries_mod = value + ": $" + str(costs[0])
            del(costs[0])
        return groceries_mod



# Test the code
print(food_costs([['apple','pear','banana'],['salmon','tuna','cod'],['milk','eggs','yogurt']],[1.99,2.99,0.99,9.99,10.99,6.99,3.49,2.49,1.49]) == 
['apple: $1.99','pear: $2.99','banana: $0.99'],['salmon: $9.99','tuna: $10.99','cod:$6.99'],['milk: $3.49','eggs: $2.49','yogurt: $1.49'])

# Question 2