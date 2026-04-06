from services import add_product,show_product,calculate_statistics,search_product,update_product,delete_product
from files import save_csv,upload_csv

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
                add_product(inventory) #lsito
            elif option ==2:
                show_product(inventory) #lsito
            elif option == 3:
                search_product(inventory) #LISTO
            elif option == 4:
                update_product(inventory) #listo
            elif option == 5:
                delete_product(inventory)#LISTO
            elif option == 6:
                calculate_statistics(inventory) #LISTOOO
            elif option == 7:
                save_csv(inventory, route='data/inventory.csv', include_header=True)
            elif option == 8:
                upload_csv()
            elif option == 9: #listo
                return print('\nThanks for used our services')
            else:
                print(f"\n{'-' * 10} Invalid input {'-' * 10}")
                choice()
        #por si se me pasa un error de value en las funciones
        except ValueError:
            print(f"\n{'-' * 10} Invalid input {'-' * 10}")
            choice()

choice()



# si el inventario esta en memoria como lista de diccionarios que le pida al usuario guardar en csv