def yesornot():
    try:
        retry = int(input(f'\nInvalid input, do you wanna try again?\n1.YES!\n2.NO!'))
        #Para que se repita cuando ingresa un numero diferente de 1 o 2
        if retry != 1 and retry != 2:
            yesornot()
        #Si ingresa alguno de los 2 numero retorna el valor
        return retry 
    #Si pone texto tiene que volver a ingresar alguna de las dos opciones
    except ValueError:
        yesornot()

def add_product(inventory):
    # Bucle para seguir pidiendo los datos del producto hasta ingresarlos correctamente, con salida
    retry = 1
    while retry != 2:
        try:
            #Ingreso de datos
            name = input('Enter the product name: ')
            price = float(input('Enter the price: '))
            quantity = int(input('Enter the quantity: '))
            retry = 2 #Salir del bucle porque respondio bien
        except ValueError: #si pasa esto es porque puso un texto al momento de ingresar un numero
            retry = yesornot()
            if retry == 2:
                return print(f"{'-' * 23}\n No products were saved\n{'-' * 23}")

    #Esquema del diccionario producto
    product = {
        'name': name,
        'price': price,
        'quantity': quantity
    }
    #Guardado de los datos del producto en la lista inventory
    inventory.append(product)
    #Print que le haga saber que los datos fueron guardados exitosamente
    return print(f'Product {name} added to inventory with price {price} and quantity {quantity}.')

def show_product(inventory):
    if not inventory:
        return print('\nInventory is empty ')
    for i,product in enumerate(inventory,1):
        print(f'{i}. Product: {product["name"]} | Price: {product ["price"]} | Quantity: {product["quantity"]} ')


def calculate_statistics(inventory):
    total_cost,total_quantity = 0, 0
    if not inventory:
        return print('\nInventory is empty ')
    for product in inventory:
        total_cost += (product["price"] * product['quantity'])
        total_quantity += product['quantity']
    print(f'The total cost of inventary are {total_cost}')
    print(f'The total cost of inventary are {total_quantity}')

