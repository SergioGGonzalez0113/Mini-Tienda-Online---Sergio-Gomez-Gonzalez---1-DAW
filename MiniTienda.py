#----Variables, listas/diccionarios/tuplas (articulos)----

articulos = [{"id": 1, "nombre": "Ratón", "precio": 12.5, "stock": 20, "activo": True}]
opcion = ""
contador = 1

#----Variables, listas/diccionarios/tuplas (usuarios)----

usuarios = [{"id": 1, "nombre": "Ana", "email": "ana@example.com", "activo": True}]
contador_usuarios = 1

#----Variables, listas/diccionarios/tuplas (carrito y ventas)----

ventas = []
carrito_actual = []
usuario_activo = None
contador_ventas = 0


# ----Definiciones de funciones (articulos)----

# imprimir menu principal
def imprimir_opciones():
    print("1. Crear artículo")
    print("2. Listar artículos")
    print("3. Buscar artículo por id")
    print("4. Actualizar artículo")
    print("5. Eliminar artículo")
    print("6. Alternar activo/inactivo")
    print("7. Usuarios")
    print("8. Ventas / Carrito")
    print("9. Salir")


# contador para aumentar id de la lista de artículos
def generar_id_articulo():
    global contador
    contador += 1
    return contador


# añadir un articulo
def generar_articulo():
    nuevo_id = generar_id_articulo()
    nombre = input("Introduce el nombre del producto: ")
    precio = float(input("Introduce el precio del producto: "))
    stock = int(input("Introduce el stock: "))
    activo = True

    nuevo_articulo = {"id": nuevo_id, "nombre": nombre, "precio": precio, "stock": stock, "activo": activo}
    articulos.append(nuevo_articulo)
    print("El artículo se ha agregado correctamente.")
    return nuevo_articulo


# Mostrar articulos
def listar_articulos():
    print(" LISTA DE ARTÍCULOS ")
    for posicion in articulos:
        print(f"ID: {posicion['id']}")
        print(f"Nombre: {posicion['nombre']}")
        print(f"Precio: {posicion['precio']}")
        print(f"Stock: {posicion['stock']}")
        print(f"Activo: {'Sí' if posicion['activo'] else 'No'}")
        print("-" * 30)
    return


# buscar un articulo por su id
def buscar_articulo_por_id(buscar):
    for producto in articulos:
        if producto["id"] == buscar:
            print(f"ID: {producto['id']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: {producto['precio']}")
            print(f"Stock: {producto['stock']}")
            print(f"Activo: {'Sí' if producto['activo'] else 'No'}")
            print("-" * 30)
            return producto
    print("No se encontró el artículo.")
    return None


# Elegir un articulo para cambiarlo
def actualizar_articulo(buscar):
    for producto in range(len(articulos)):
        if articulos[producto]["id"] == buscar:
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
            print("Artículo actualizado correctamente.")
            return
    print("No se encontró el artículo.")


# eliminar un articulo
def eliminar_articulo(buscar):
    for producto in range(len(articulos) - 1, -1, -1):
        if articulos[producto]["id"] == buscar:
            print(f"Se borrará el artículo {articulos[producto]}")
            del articulos[producto]
            print("Se ha eliminado correctamente.")
    return


# Cambiar activo
def alternar_activo(buscar):
    for producto in articulos:
        if producto["id"] == buscar:
            nuevo_activo = input("Indicador de activo: s o n: ")
            if nuevo_activo == "s":
                producto["activo"] = True
            elif nuevo_activo == "n":
                producto["activo"] = False
            print("Estado actualizado.")
            return
    print("No se encontró el artículo.")


# ----Definiciones de funciones (usuarios)----

def menu_usuarios():
    global opcion_usuarios
    opcion_usuarios = ""
    while opcion_usuarios != "7":
        imprimir_opciones_usuarios()
        opcion_usuarios = input("¿Qué quieres hacer? ")
        match opcion_usuarios:
            case "1":
                crear_usuario()
            case "2":
                listar_usuarios()
            case "3":
                buscar = int(input("Introduce la id del usuario a buscar: "))
                buscar_usuario_por_id(buscar)
            case "4":
                buscar = int(input("Introduce la id del usuario a modificar: "))
                actualizar_usuario(buscar)
            case "5":
                buscar = int(input("Introduce la id del usuario a eliminar: "))
                eliminar_usuario(buscar)
            case "6":
                buscar = int(input("Introduce la id del usuario a alternar activo: "))
                alternar_activo_usuario(buscar)
            case "7":
                print("Volviendo...")
                return

    #Mostrar opciones de usuario
def imprimir_opciones_usuarios():
    print("1. Crear usuario")
    print("2. Listar usuarios")
    print("3. Buscar usuario por id")
    print("4. Actualizar usuario")
    print("5. Eliminar usuario")
    print("6. Alternar activo/inactivo")
    print("7. Volver")


def generar_id_usuario():
    global contador_usuarios
    contador_usuarios += 1
    return contador_usuarios

    #Crear un nuevo usuario
def crear_usuario():
    nuevo_id = generar_id_usuario()
    usuario = input("Introduce el nombre del usuario: ")
    email = input("Introduce el email del usuario: ")
    activo = True

    nuevo_usuario = {"id": nuevo_id, "nombre": usuario, "email": email, "activo": activo}
    usuarios.append(nuevo_usuario)
    print("El usuario se ha registrado correctamente.")
    return nuevo_usuario

    #Mostrar los usuarios
def listar_usuarios():
    print(" LISTA DE USUARIOS ")
    for posicion in usuarios:
        print(f"ID: {posicion['id']}")
        print(f"Nombre: {posicion['nombre']}")
        print(f"Email: {posicion['email']}")
        print(f"Activo: {'Sí' if posicion['activo'] else 'No'}")
        print("-" * 30)
    return

    #Buscar un usuario por su id
def buscar_usuario_por_id(buscar):
    for usuario in usuarios:
        if usuario["id"] == buscar:
            print(f"ID: {usuario['id']}")
            print(f"Nombre: {usuario['nombre']}")
            print(f"Email: {usuario['email']}")
            print(f"Activo: {'Sí' if usuario['activo'] else 'No'}")
            print("-" * 30)
            return usuario
    print("No se encontró el usuario.")
    return None

    #Actualizar un usuario existente
def actualizar_usuario(buscar):
    for usuario in range(len(usuarios)):
        if usuarios[usuario]["id"] == buscar:
            nuevo_nombre = input("Introduce el nuevo nombre del usuario: ")
            usuarios[usuario]["nombre"] = nuevo_nombre

            nuevo_email = input("Introduce el nuevo email del usuario: ")
            usuarios[usuario]["email"] = nuevo_email

            nuevo_activo = input("Indicador de activo: s o n: ")
            if nuevo_activo == "s":
                usuarios[usuario]["activo"] = True
            elif nuevo_activo == "n":
                usuarios[usuario]["activo"] = False
            print("Usuario actualizado correctamente.")
            return
    print("No se encontró el usuario.")

    #Eliminar un usuario
def eliminar_usuario(buscar):
    for usuario in range(len(usuarios) - 1, -1, -1):
        if usuarios[usuario]["id"] == buscar:
            print(f"Se borrará el usuario {usuarios[usuario]}")
            del usuarios[usuario]
            print("Se ha eliminado correctamente.")
    return

    #Modificar el activo de un usuario
def alternar_activo_usuario(buscar):
    for usuario in usuarios:
        if usuario["id"] == buscar:
            nuevo_activo = input("Indicador de activo: s o n: ")
            if nuevo_activo == "s":
                usuario["activo"] = True
            elif nuevo_activo == "n":
                usuario["activo"] = False
            print("Estado actualizado.")
            return
    print("No se encontró el usuario.")


# ----Definiciones de funciones (ventas y carrito)----

    #Mostrar menu de ventas
def menu_ventas():
    global usuario_activo
    opcion_ventas = ""
    while opcion_ventas != "8":
        imprimir_opciones_ventas()
        opcion_ventas = input("¿Qué quieres hacer? ")
        match opcion_ventas:
            case "1":
                usuario_activo = elegir_usuario_activo()
            case "2":
                añadir_al_carrito()
            case "3":
                quitar_del_carrito()
            case "4":
                ver_carrito()
            case "5":
                confirmar_compra()
            case "6":
                if usuario_activo is not None:
                    historial_ventas_por_usuario(usuario_activo)
                else:
                    print("No hay usuario activo seleccionado.")
            case "7":
                vaciar_carrito()
            case "8":
                print("Volviendo al menú principal...")

    #Mostrar opciones de ventas y carrito
def imprimir_opciones_ventas():
    print("1. Seleccionar usuario activo")
    print("2. Añadir artículo al carrito")
    print("3. Quitar artículo del carrito")
    print("4. Ver carrito (detalle y total)")
    print("5. Confirmar compra (resta stock y registra venta)")
    print("6. Historial de ventas por usuario")
    print("7. Vaciar carrito")
    print("8. Volver")

    #Elegir un usuario activo
def elegir_usuario_activo():
    listar_usuarios()
    buscar = int(input("Introduce la id del usuario activo: "))
    for usuarioA in usuarios:
        if usuarioA["id"] == buscar and usuarioA["activo"]:
            print(f"Usuario activo: {usuarioA['nombre']}")
            return usuarioA["id"]
    print("El usuario no existe o está inactivo.")
    return None

    #Añadir un producto al carrito
def añadir_al_carrito():
    global carrito_actual
    if usuario_activo is None:
        print("Para comprar un artículo debes seleccionar un usuario activo.")
        return
    listar_articulos()
    articulo_id = int(input("Introduce la id del artículo que quieres añadir: "))
    articulo = None
    for art in articulos:
        if art["id"] == articulo_id and art["activo"]:
            articulo = art
    if articulo is None:
        print("El artículo no está disponible.")
        return
    cantidad = int(input("¿Qué cantidad de este producto deseas comprar? "))
    if cantidad < 1:
        print("Cantidad inválida.")
        return
    if cantidad > articulo["stock"]:
        print("No hay suficiente cantidad de este producto.")
        return
    encontrado = False
    for i in range(len(carrito_actual)):
        if carrito_actual[i][0] == articulo_id:
            nueva_cantidad = carrito_actual[i][1] + cantidad
            if nueva_cantidad > articulo["stock"]:
                print("La cantidad total supera el stock.")
                return
            carrito_actual[i] = (articulo_id, nueva_cantidad)
            encontrado = True
    if not encontrado:
        carrito_actual.append((articulo_id, cantidad))
    print("Artículo añadido al carrito correctamente.")

    #Quitar del carrito un producto
def quitar_del_carrito():
    global carrito_actual
    if len(carrito_actual) == 0:
        print("El carrito está vacío.")
        return
    articulo_id = int(input("Introduce la id del artículo que quieres quitar del carrito: "))
    nuevo_carrito = []
    eliminado = False
    for elemento_carrito in carrito_actual:
        if elemento_carrito[0] == articulo_id:
            eliminado = True
        else:
            nuevo_carrito.append(elemento_carrito)
    carrito_actual = nuevo_carrito
    if eliminado:
        print("El artículo se ha eliminado del carrito.")
    else:
        print("El artículo no está en el carrito.")

    #Mostrar el carrito
def ver_carrito():
    if len(carrito_actual) == 0:
        print("El carrito está vacío.")
        return
    print("=== CARRITO ACTUAL ===")
    total = 0
    for elemento_carrito in carrito_actual:
        articulo_id, cantidad = elemento_carrito
        for elemento_articulos in articulos:
            if elemento_articulos["id"] == articulo_id:
                subtotal = cantidad * elemento_articulos["precio"]
                print(f"{elemento_articulos['nombre']} x {cantidad} = {subtotal}€")
                total += subtotal
    print(f"TOTAL: {total}€")
    return total

    #Confirmar la compra de un usuario
def confirmar_compra():
    global contador_ventas, carrito_actual
    if usuario_activo is None:
        print("No hay usuario activo.")
        return
    if len(carrito_actual) == 0:
        print("El carrito está vacío.")
        return
    for elemento_carrito in carrito_actual:
        articulo_id, cantidad = elemento_carrito
        articulo = None
        for elemento_articulos in articulos:
            if elemento_articulos["id"] == articulo_id:
                articulo = elemento_articulos
        if articulo is None or not articulo["activo"]:
            print("Uno de los artículos no está disponible o activo.")
            return
        if cantidad > articulo["stock"]:
            print("No hay cantidad suficiente de uno de los artículos.")
            return
    elementos_venta = []
    total = 0
    for elemento_carrito in carrito_actual:
        articulo_id, cantidad = elemento_carrito
        for elementos_articulos in articulos:
            if elementos_articulos["id"] == articulo_id:
                elementos_articulos["stock"] -= cantidad
                subtotal = cantidad * elementos_articulos["precio"]
                elementos_venta.append((articulo_id, cantidad, elementos_articulos["precio"]))
                total += subtotal
    contador_ventas += 1
    venta = {"id_venta": contador_ventas, "usuario_id": usuario_activo, "items": elementos_venta, "total": total}
    ventas.append(venta)
    carrito_actual = []
    print(f"Compra realizada. Total: {total}€.")

    #Historial de ventas de usuarios
def historial_ventas_por_usuario(usuario_id):
    print(" - - - HISTORIAL DE VENTAS POR USUARIO - - -")
    encontrado = False
    for venta in ventas:
        if venta["usuario_id"] == usuario_id:
            encontrado = True
            print(f"ID Venta: {venta['id_venta']} - Total: {venta['total']}€")
            for elemento_ventas in venta["items"]:
                articulo_id, cantidad, precio = elemento_ventas
                for elemento_articulo in articulos:
                    if elemento_articulo["id"] == articulo_id:
                        nombre = elemento_articulo["nombre"]
                        print(f"{nombre} x {cantidad} - {precio}€ c/u")
            print("-" * 40)
    if not encontrado:
        print("No hay ventas registradas para este usuario.")

    #Vaciar el carrito
def vaciar_carrito():
    global carrito_actual
    carrito_actual = []
    print("El carrito se ha vaciado correctamente.")


#----Lógica principal ----

while opcion != "9":
    imprimir_opciones()
    opcion = input("¿Qué quieres hacer? ")
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
        case "6":
            buscar = int(input("Introduce la id del artículo a alternar activo: "))
            alternar_activo(buscar)
        case "7":
            menu_usuarios()
        case "8":
            menu_ventas()
        case "9":
            print("Hasta luego...")

