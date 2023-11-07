# This is a supermarket.
# It has multiple departments and and different types of clerks and workers that can either interact or not with the customers

# Departments: Meat, Seafood, Deli, organic_foods, care_products, health_and_beauty, fruit, tet_items, snacks, bread_isle,
# condiments_isle, pasta_isle, alcohol_isle, bakery, dairy, produce, frozen, cereal, front_ens, back_end

# People: Cashiers, cooks, customers, cleaners, stockers, warehouse_workers, farmacists, wine_specialists, managers, supervisors.

# am / pm shifts, overnight crew

# Only manager can purchase inventory
# Only cooks allowed in kitchen
# no customes allowed in back_end area
# all customers and all workers can purchase, they need to have a wallet
# all itrms have a 'key: value' = 'item: price', prices to be deducted from wallet, if not enough money in wallet, pop and delete an itmem,
# this would be like a return
# inventory is affected by item purchased

print()
print("Welcome to Good Day; your neighborhood supermarket!")
print()
print("We have a vast variety of departments stock with some of the best products, where would you like start today?")
print()

departments = ["Meat", "Seafood", "Deli", "Organic Foods", "Care Products", "Health and Beauty", "Fruit", "Snacks", "Bread",
               "Condiments", "Pasta", "Alcohol", "Bakery", "Dairy", "Produce", "Frozen", "Cereal", "Front end", "Back end"]
departments.sort()
departments_length = len(departments)
index = 0
print("Please choose where you´d like to start: ")
while index < departments_length:
    print((departments[index]))
    index += 1
print("Please enter the department you'd like to start: ")
