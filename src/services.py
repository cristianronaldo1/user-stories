#Mejor hice una funcion que dependiendo si son 2 o 3 options le permita esoger, pero esto es para cuando el lindo usuario pone un bellaco texto en vez de numero ;)
def options_(end,start):
    # 2 - 1 = 1
    if end - start == 1:
        # devulve el numero de la opcion escogida
        def yesornot():
            try:
                retry = int(input(f'\nInvalid input, do you wanna try again?\n1.YES!\n2.NO!'))
                #Para que se repita cuando ingresa un numero diferente de 1 o 2
                if retry != 1 and retry != 2:
                    return yesornot()
                #Si ingresa alguno de los 2 numero retorna el valor
                return retry 
            #Si pone texto tiene que volver a ingresar alguna de las dos opciones
            except ValueError:
                return yesornot()
        return yesornot()
    # 4 - 1 = 2 pero más facil con else porque esto ya lo pongo yo jiji
    else:
        # devulve el numero de la opcion escogida
        def thr_option():
            try:
                retry = int(input(f'\nEnter your option...\n1.Name!\n2.Price!\n3.Quantity \n4.None'))
                #Para que se repita cuando ingresa un numero diferente de 1 o 2
                if retry != 1 and retry != 2 and retry != 3 and retry != 4:
                    thr_option()
                #Si ingresa alguno de los 3 numero retorna el valor
                return retry 
            #Si pone texto tiene que volver a ingresar alguna de las dos opciones
            except ValueError:
                print('\nInvalid input')
                thr_option()
        return thr_option()


# Mejor una funcion que valide directamente los datos, porque se estan ingresando varias veces los datos y mejor es en una funcion para no escribir tanto jajajja
def get_product_data():
    retry = 1
    # Bucle para seguir pidiendo los datos del producto hasta ingresarlos correctamente, con salida
    while retry != 2:
        try:
            #Ingreso de datos
            print('\nNote: Do not use spaces or accents unless necessary.') #como hay productos que puede que tengan espacios en la mitad por eso pongo esto y no un punto replace(" ","")
            name = input('Enter the product name: ').strip().lower() #Quitar los espacios de los extremos y poner en minuscula todo 
            price = float(input('Enter the price: '))
            quantity = int(input('Enter the quantity: '))
            return name, price, quantity
        except ValueError: #si pasa esto es porque puso un texto al momento de ingresar un numero
            retry = options_(2,1) #Devuelve el numero de la opcion escogida, en una función aparte se ve más cool
            if retry == 2:
                return None #return none asi es más facil de manejarlo cuando obtenga los datos al momento de invocarse



def add_product(inventory): #1 ---

    result = get_product_data()
    #Si no es none es porque si guardo algo
    if result is not None:
        name, price, quantity = result
    else:
        return print('No products were saved')

    # Verificar si ya esta agregado o no, esto devuelve un boolean
    added = any(product['name'] == name for product in inventory)
    if added:
        return print('This product has already been added!')
    else:
        #Esquema del diccionario producto
        product = {
            'name': name,
            'price': price,
            'quantity': quantity
        }
        #Guardado de los datos del producto en la lista inventory SI no esta en la lista
        inventory.append(product)
        #Print que le haga saber que los datos fueron guardados exitosamente
        return print(f"Product '{name}' added to inventory with price {price} and quantity {quantity}.")

def show_product(inventory): #2 ---
    if not inventory:
        return print(f"{'-' * 10}Inventory is empty {'-' * 10} ")
    # Va a mostar los productos en orden 
    for i,product in enumerate(inventory,1):
        print(f'{i}. Product: {product["name"]} | Price: {product ["price"]} | Quantity: {product["quantity"]} ')

def search_product (inventory): #3 ---
    name = input('\nEnter the product name to search: ').strip().lower()
    for product in inventory:
        if product['name'] == name:
            return print(f'Product found!\n {product}')
        else:
            return print(f" {'-' * 10} Error 404!\nProduct not found! {'-' * 10}")

def update_product(inventory): #4 ---
    name = input('\nEnter the product name to update: ').strip().lower()
    option = int(input('\nDo you like chage everything or not?\n1.YES!\n2.NO!'))
    while option > 0 and option < 3:
        #Recorer para encontrarlo y update
        for product in inventory:
            if product['name'] == name: #Si lo encuentra update

                if option == 1: #si quiere cambiar todo
                    #pedir los 3 datos y update
                    result = get_product_data()
                    if result is not None: #Osea si guardo los datos
                        name, price, quantity = result
                        product['name'], product['price'], product['quantity'] = name, price, quantity
                        return print(f"\nProduct '{name}' update to inventory with price {price} and quantity {quantity}.")
                    else:
                        return print(f"{'-' * 10} No products were saved {'-' * 10}")   
                            
                elif option == 2:# No quiere cambiar todo, osea algo en especifico
                    option = options_(4,1)
                    #reemplazar los datos
                    if option == 1:
                        product['name'] == input('Enter the product name to update:')
                        return print(f"Product '{name}' updated to inventory  ")
                    elif option == 2:
                        product['price'] == float(input('Enter the product price to update:'))
                        return print(f"Product '{name}' updated to inventory with price {price} ")
                    elif option == 3:
                        product['quantity'] == int(input('Enter the product quantity to update:'))
                        return print(f"Product '{name}' updated to inventory with quantity {quantity} ")
                    else:
                        return print(f"{'-' * 10} No products have been updated! {'-' * 10}")
            #dato no encontrado
            else:
                return print(f"{'-' * 10} Product no found to update! {'-' * 10}")



def delete_product(inventory): #5 ---
    name = input('\nEnter the product name to delete: ').strip().lower()
    for product in inventory:
        if product['name'] == name:
            inventory.remove(product)
            return print(f"Product! '{name}' deleted  ")
            
        else:
            return print(f"{'-' * 10} Error 404!  Product not found! {'-' * 10}")

def calculate_statistics(inventory): #6 ---
    total_cost,total_quantity, expensive_product, larger_inventory,expensive, larger = 0, 0, "", "", 0.0, 0
    if not inventory:
        return print('\nInventory is empty ')
    for product in inventory:
        total_cost += (product["price"] * product['quantity'])
        total_quantity += product['quantity']
        
        if product['price'] > expensive:
            expensive = product['price']
            expensive_product = f"The most expensive product is: {product['name']} with price {product['price']}"

        if product['quantity'] > larger:
            larger = product['quantity']
            larger_inventory = f"The most larger product is: {product['name']} with quantity {product['quantity']}"

    print(f'The total cost of inventary are {total_cost}')
    print(f'The total cost of inventary are {total_quantity}')
    print(expensive_product)
    print(larger_inventory)

