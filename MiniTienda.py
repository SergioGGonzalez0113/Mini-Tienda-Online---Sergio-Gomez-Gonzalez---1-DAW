#----Variables, listas/diccionarios/tuplas----

articulos = [{"id": 1, "nombre": "Ratón", "precio": 12.5, "stock": 20, "activo": True}]
opcion = ""
contador = 1

# ----Definiciones de funciones----
    
    #imprimir menu
def imprimir_opciones():
    print("1. Crear artículo")
    print("2. Listar artículos")
    print("3. Buscar artículo por id")
    print("4. Actualizar artículo")
    print("5. Eliminar artículo")
    print("6. Alternar activo/inactivo")
    print("7. Salir")

    #contador para aumentar id de la lista
def generar_id():
    global contador 
    contador += 1
    return contador
    
    #añadir un articulo
def generar_articulo():
    nuevo_id = generar_id()
    nombre = input("Introduce el nombre del producto: ")
    precio = float(input("Introduce el precio del producto: "))
    stock = int(input("Introduce el stock: "))
    activo = True

    
    nuevo_articulo = {"id": nuevo_id, "nombre": nombre, "precio": precio, "stock": stock,"activo": activo}
    articulos.append(nuevo_articulo)
    print("El artículo se ha agregado correctamente ")
    return nuevo_articulo

    #Mostrar articulos
def listar_articulos():
    print(" LISTA DE ARTÍCULOS ACTIVOS ")

    for posicion in articulos:
        print(f"ID: {posicion['id']}")
        print(f"Nombre: {posicion['nombre']}")
        print(f"Precio: {posicion['precio']}")
        print(f"Stock: {posicion['stock']}")
        print(f"Activo: {'Sí' if posicion['activo'] else 'No'}")
        print("- - - - - - - - - - - - - - - ")
    return

    #buscar un articulo por su id
def buscar_articulo_por_id(buscar):
  
    for producto in range(len(articulos)):
        if articulos[producto]["id"] == buscar:
            producto = articulos[producto]
            print(f"ID: {producto['id']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: {producto['precio']}")
            print(f"Stock: {producto['stock']}")
            print(f"Activo: {'Sí' if producto['activo'] else 'No'}")
            print("- - - - - - - - - - - - - - - ")
    return producto
    
    #Elegir un articulo para cambiarlo    
def actualizar_articulo(buscar):
    for producto in range(len(articulos)):
        if articulos[producto]["id"] == buscar:
            articulo_encontrado = articulos[producto]
    nuevo_nombre = input("Introduce el nuevo nombre del producto: ")
    articulos[producto]["nombre"] = nuevo_nombre

    nuevo_precio = float(input("Introduce el nuevo precio del producto: "))
    articulos[producto]["precio"] = nuevo_precio

    nuevo_stock = int(input("Introduce el nuevo stock del producto: "))
    articulos[producto]["stock"] = nuevo_stock

    nuevo_activo = input("Indicador de activo: s o n: ")
    if nuevo_activo == "s":
        articulos[producto]["activo"] = True
    elif nuevo_activo == "n":
        articulos[producto]["activo"] = False
    return

    #eliminar un articulo
def eliminar_articulo(buscar):
    for producto in range(len(articulos) - 1, -1, -1):
        if articulos[producto]["id"] == buscar:
            print(f"Se borrará el artículo {articulos[producto]}")
            del articulos[producto]
            print("Se ha eliminado correctamente ")
             
    return
    
    #Cambiar activo     
def alternar_activo(buscar):
    for producto in range(len(articulos)):
        if articulos[producto]["id"] == buscar:
            articulo_encontrado = articulos[producto]
    
    nuevo_activo = input("Indicador de activo: s o n: ")
    if nuevo_activo == "s":
        articulos[producto]["activo"] = True
    elif nuevo_activo == "n":
        articulos[producto]["activo"] = False
    return     
             
     


#----Logica y funcionamiento----

while opcion != "7":
    imprimir_opciones()
    opcion = (input("¿Qué quieres hacer? "))
    match opcion:
        
        case "1":
                generar_articulo()
        case "2":
                listar_articulos()
        case "3":
                buscar = int(input("Introduce la id del artículo a buscar: "))
                buscar_articulo_por_id(buscar)
        case "4":
                buscar = int(input("Introduce la id del artículo a modificar: "))
                actualizar_articulo(buscar)
        case "5":
                buscar = int(input("Introduce la id del artículo a eliminar: "))
                eliminar_articulo(buscar) 
        case"6":
                buscar = int(input("Introduce la id del artículo a alternar activo: "))
                alternar_activo(buscar)
        case"7":
                print("Hasta luego. . .")
              
              

        

            
            




