from ejercicio1.calzado import Calzado
from ejercicio1.calzado_admin import CalzadoAdmin
from ejercicio1.calzado_tipo import CalzadoTipo
from ejercicio1.calzado_color import CalzadoColor
from ejercicio1.calzado_talle import CalzadoTalle

def main():
    # Crear instancias de tipos, colores y talles
    tipo_deportivo = CalzadoTipo("Deportivo")
    tipo_casual = CalzadoTipo("Casual")
    tipo_formal = CalzadoTipo("Formal")

    color_negro = CalzadoColor("Negro")
    color_blanco = CalzadoColor("Blanco", "Blanco")
    color_rojo = CalzadoColor("Rojo", "Negro")

    talle_40 = CalzadoTalle("40", 26.5)
    talle_42 = CalzadoTalle("42", 27.5)
    talle_44 = CalzadoTalle("44", 28.5)

    # Crear instancia de CalzadoAdmin
    admin = CalzadoAdmin()

    # Crear 5 instancias de Calzado
    calzado1 = Calzado(1, "Nike Air", "Zapatillas deportivas", tipo_deportivo, talle_40, color_negro, 10, 120.0)
    calzado2 = Calzado(2, "Adidas Retro", "Zapatillas casuales", tipo_casual, talle_42, color_blanco, 5, 80.0)
    calzado3 = Calzado(3, "Puma Elegant", "Zapatos formales", tipo_formal, talle_44, color_negro, 3, 150.0)
    calzado4 = Calzado(4, "Reebok Sport", "Zapatillas running", tipo_deportivo, talle_40, color_rojo, 8, 150.0)
    calzado5 = Calzado(5, "Converse Classic", "Zapatillas clásicas", tipo_casual, talle_42, color_blanco, 12, 70.0)

    # Probar agregar_calzado
    print("Agregando calzados...")
    admin.agregar_calzado(calzado1)
    admin.agregar_calzado(calzado2)
    admin.agregar_calzado(calzado3)
    admin.agregar_calzado(calzado4)
    admin.agregar_calzado(calzado5)
    print("Calzados agregados exitosamente.")

    # Probar buscar_calzado
    print("\nBuscando calzado con SKU 2:")
    encontrado = admin.buscar_calzado(2)
    if encontrado:
        print(encontrado)
    else:
        print("No encontrado")

    # Probar filtrar_por_tipo
    print("\nFiltrando por tipo Deportivo:")
    deportivos = admin.filtrar_por_tipo(tipo_deportivo)
    for calzado in deportivos:
        print(calzado)

    # Probar filtrar_precio_entre
    print("\nFiltrando precio entre 70 y 120:")
    filtrados_precio = admin.filtrar_precio_entre(70, 120)
    for calzado in filtrados_precio:
        print(calzado)

    # Probar cantidad_productos
    print(f"\nCantidad total de productos: {admin.cantidad_productos()}")

    # Probar total_productos
    print(f"Total importe de productos: ${admin.total_productos()}")

    # Probar modificar_calzado
    print("\nModificando calzado con SKU 1...")
    calzado_modificado = Calzado(1, "Nike Air Max", "Zapatillas deportivas premium", tipo_deportivo, talle_40, color_negro, 15, 140.0)
    admin.modificar_calzado(calzado_modificado)
    print("Calzado modificado.")

    # Verificar modificación
    print("Buscando calzado modificado:")
    modificado = admin.buscar_calzado(1)
    if modificado:
        print(modificado)

    # Probar eliminar_calzado
    print("\nEliminando calzado con SKU 5...")
    admin.eliminar_calzado(5)
    print("Calzado eliminado.")

    # Verificar eliminación
    print("Buscando calzado eliminado:")
    eliminado = admin.buscar_calzado(5)
    if eliminado:
        print(eliminado)
    else:
        print("No encontrado (correcto)")

    print(f"\nNueva cantidad total de productos: {admin.cantidad_productos()}")
    print(f"Nuevo total importe de productos: ${admin.total_productos()}")

if __name__ == '__main__':
    main()