# This program calculates the total value of stock in the cafe'.

# The list at Line 4 contains the items which are sold within the cafe'.
menu = ["Cinnamon Swirl", "Rockie Road", "Blueberry Muffin", "Chocolate Brownie"]

stock = {menu[0]: 5,    # This dictionary contains the stock value for each item on the menu.
         menu[1]: 2,    # The keys of the dictionary are set to the corresponding indices of
         menu[2]: 1,    # the 'menu' list. The stock values are stored next to each key within
         menu[3]: 6     # the dictionary. 
        }

price = {menu[0]: 3,    # This dictionary contains the price value for each item on the menu.
         menu[1]: 2,    # The keys of the dictionary are set to the corresponding indices of
         menu[2]: 2.5,  # the 'menu' list. The price values are stored next to each key within
         menu[3]: 2.75  # the dictionary.
        }

total_items = [stock[i] * price[i] for i in menu]   # This for loop calculates the total value of
                                                    # each item when multiplied by the quantity 
                                                    # of that item. 

total_stock = 0 # This variable has been delcared to count the total stock which is calculated
                # at Lines 25 and 26.

for i in total_items:               # This for loop calculates the total value of 
    total_stock = total_stock + i   # the items in the cafe which were
                                    # multiplied by their quantities at Line 18. 

# The total stock is printed for the user at Line 30. 
print("The total stock of the cafe' is ${}".format(str(total_stock)))

