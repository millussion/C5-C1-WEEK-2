from functions import *
def menu(inventory):
    running = True
    while running:
        print("INVENTORY")
        print("1. Add product")
        print("2. Show product")
        print("3. View Stats")
        print("4. Exit")

        option = input("Enter a option: ")
        if option == "1":
            add_products(inventory)
            print(inventory)
        if option == "2":
            show_product(inventory)
        if option == "3":
            show_stats(inventory)
        if option == "4":
            print("Exiting")
            running = False