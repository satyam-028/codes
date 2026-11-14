menu = {
    "pizza":50,
    "momos":50,
    "pasta":50,
    "coffee":50,
}
print("welcome to restraurant!!!")
print("pizza: Rs.50\nmomos: Rs.50\npasta: Rs.50\ncoffee: Rs.50")

order_total = 0

item_1 = input("Enter the name of item you want to order = ")

while True:
    if item_1 in menu:
        order_total += menu[item_1]
        print(f"Your item {item_1} has been added to order")

    else:
        print(f"Ordered item {item_1} is not present yet")

    another_order = input("DO you want to add same other items? (Yes/No) ")
    if another_order == "yes":
        item_2 = input("Enter the name of item = ")
        if item_2 in menu:
           order_total += menu[item_2]
           print(f"Your item {item_2} has been added to order")
        
        else:
           print(f"Ordered item {item_2} is not present yet")
           
        
    print(f"The total amount of items to pay is = {order_total}")
  