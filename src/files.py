import csv, os

def checks_csv():
    #devuelve una lista con todos los nombres de archivos que hay en esa carpeta
    files = os.listdir("data")
    csv_files = [f for f in files if f.endswith(".csv")] #recorre todos los archivos para que guarde cuales son los csv
    
    #guarde el unico que haya csv
    if len(csv_files) == 1:
        return f'data/{csv_files[0]}'
    elif len(csv_files) > 1:
        print(f"These .csv files have been found\n{csv_files}")
        file = input("Enter the file name with the extension:  ")
        for f in csv_files:
            if f == file:
                return file # que retorne el nombre del archivo ingresado
        # Ingreso mal el nombre del csv
        return None
    else:
        return None



#a
#w
#r
#xn
def save_csv(inventory,route, include_header):
    if not inventory:
        return print(f"{'-' * 10}Inventory is empty {'-' * 10} ")
    
    try:
        #Si no tiene header se pone en modo w para sobrescribir, si no a para agregar
        mode = 'w' if include_header else 'a'
        with open(route, mode, encoding="utf-8", newline='') as file:
            writer = csv.writer(file)
            
            if include_header:
                writer.writerow(['Name','Price','Quantity'])
                include_header = False

                for product in inventory:
                    writer.writerow([product['name'],product['price'], product['quantity']])
                
            return print('The data has been successfully saved')
            
            
    except PermissionError:
        #no se porque tengo que poner esto :/
        return print(f"{'-' * 10} You don't have write permissions {'-' * 10}")
    except Exception as e:
        return print(f"{'-' * 10} General error saving the file {'-' * 10}\n {e}")

def upload_csv():
    try:
        route = checks_csv()  # Busca archivos CSV en data
        if route is None:
            return print(f"{'-' * 10} There are no CSV files or the name you entered is incorrect {'-' * 10}")

        with open(route, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)  
            header = next(reader)  # Lee solo la primera fila (el encabezado) y avanza el cursor

            # +si no son exactamente 3 columnas, falla
            try:
                col_name, col_price, col_quantity = header
            except ValueError:
                return print(f"{'-' * 10} Error in the expected header; this file cannot be loaded {'-' * 10}")

            # Valida que los nombres del encabezado sean los esperados sin importar mayúsculas/espacios
            expected = ['name', 'price', 'quantity']
            if [col.lower().strip() for col in header] != expected:
                return print(f"{'-' * 10} The header doesn't match the expected format {'-' * 10}")

            inventory = []  #  se acumulan los productos buenos
            # enumerate empieza en 2 porque la fila 1 es el header
            for i, row in enumerate(reader, start=2):
                try:
                    name, price, quantity = row  # Desempaca cada fila en 3 valores
                    inventory.append({
                        'name': name.strip(),       # Elimina espacios sobrantes
                        'price': float(price),       # Convierte de string a decimal
                        'quantity': int(quantity)     # Convierte de string a entero
                    })
                except ValueError:
                    # Si la fila tiene datos que no se pueden convertir, la salta
                    print(f"Row {i} skipped (bad data): {row}")

        print(f"{len(inventory)} products loaded successfully")
        return inventory 

    except FileNotFoundError:
        print(f"{'-' * 10} File not found {'-' * 10}")
    except Exception as e:
        print(f"{'-' * 10} General error loading the file {'-' * 10}\n {e}")
            
