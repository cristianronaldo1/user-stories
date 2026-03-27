from inventory import add_product,show_product,calculate_statistics

inventory = []


print("\n--- Welcome to Olimpica ---")

def choice():
    option = 1
    while option > 0 and option < 10:
        try:
            option = int(input("""\nEnter what you want to do:
1. Add product
2. Show product
3. Search product
4. Update product
5. Delete product
6. Inventory Statistics
7. Save inventory to CSV
8. Load inventory from CSV
9. Exit
..."""))

            if option == 1:
                add_product(inventory)
            elif option ==2:
                show_product(inventory)
            elif option == 3:
                pass
            elif option == 4:
                pass
            elif option == 5:
                pass
            elif option == 6:
                calculate_statistics(inventory)
            elif option == 7:
                pass
            elif option == 8:
                pass
            elif option == 9:
                pass
            else:
                print(f"\n{'-' * 10} Invalid input {'-' * 10}")
                choice()
        except ValueError:
            print(f"\n{'-' * 10} Invalid input {'-' * 10}")
            choice()

choice()



# si el inventario esta en memoria como lista de diccionarios que le pida al usuario guardar en csv