menu = ["Cinnamon Swirl", "Rockie Road", "Blueberry Muffin", "Chocolate Brownie"]

stock = {menu[0]: 5,
         menu[1]: 2,
         menu[2]: 1,
         menu[3]: 6
        }

price = {menu[0]: 3,
         menu[1]: 2,
         menu[2]: 2.5,
         menu[3]: 2.75
        }

total_items = [stock[i] * price[i] for i in menu]

total_stock = 0

for i in total_items:
    total_stock = total_stock + i

print(total_stock)

