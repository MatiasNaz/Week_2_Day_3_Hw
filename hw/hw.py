# Hw Exercise 1:
# Create Shopping Cart
# Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?


def shopping_cart():
    cart = {}
    while True:
        question = input(
            "Would you like to [S]how cart, [A]dd item [D]elete or [Q]uit? ")
        if question.lower() == 's':
            print(cart)
        if question.lower() == 'a':
            item = input(
                "Please enter the item you would like to add to shopping cart: ")
            quantity = input("How many would you like? ")
            cart[item] = quantity
        if question.lower() == 'd':
            cart.pop(item)
        if question.lower() == 'q':
            print("Here's your final order, thanks for shopping with us")
            print('====================================================')
            print(cart)
            break


shopping_cart()

