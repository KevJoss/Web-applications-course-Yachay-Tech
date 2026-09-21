import json
import requests


BASE_URL = "http://127.0.0.1:8000"


def show_response(response):
    """Muestra la respuesta del servidor de forma legible"""
    print()
    print("=" * 50)
    print(f"HTTP: {response.status_code}")
    print("=" * 50)
    
    try:
        print(json.dumps(response.json(), indent=4))
    except Exception:
        print(response.text)
    print()


def create_customer():
    """Opción 1: Crear un cliente"""
    name = input("Nombre del cliente: ")
    email = input("Email: ")

    data = {
        "name": name,
        "email": email
    }

    response = requests.post(
        f"{BASE_URL}/customers",
        json=data
    )

    show_response(response)


def list_customers():
    """Opción 2: Listar todos los clientes"""
    response = requests.get(f"{BASE_URL}/customers")
    show_response(response)


def create_product():
    """Opción 3: Crear un producto"""
    name = input("Nombre del producto: ")
    price = input("Precio: ")
    stock = int(input("Stock: "))

    data = {
        "name": name,
        "price": price,
        "stock": stock
    }

    response = requests.post(
        f"{BASE_URL}/products",
        json=data
    )

    show_response(response)


def list_products():
    """Opción 4: Listar todos los productos"""
    response = requests.get(f"{BASE_URL}/products")
    show_response(response)


def create_order_from_json():
    """Opción 5: Crear una orden desde JSON"""
    filename = input("Archivo JSON [client/data/order.json]: ")

    if filename.strip() == "":
        filename = "client/data/order.json"

    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        response = requests.post(
            f"{BASE_URL}/orders",
            json=data
        )

        show_response(response)

    except FileNotFoundError:
        print(f"Archivo no encontrado: {filename}")


def show_order():
    """Opción 6: Ver una orden específica"""
    order_id = input("ID de la orden: ")

    response = requests.get(f"{BASE_URL}/orders/{order_id}")
    show_response(response)


def show_customer_orders():
    """Opción 7: Ver órdenes de un cliente"""
    customer_id = input("ID del cliente: ")

    response = requests.get(f"{BASE_URL}/customers/{customer_id}/orders")
    show_response(response)


def update_order_status():
    """Opción 8: Actualizar estado de una orden"""
    order_id = input("ID de la orden: ")
    status = input("Nuevo estado (pending/completed/cancelled): ")

    data = {"status": status}

    response = requests.put(
        f"{BASE_URL}/orders/{order_id}/status",
        json=data
    )

    show_response(response)


def delete_order():
    """Opción 9: Eliminar una orden"""
    order_id = input("ID de la orden: ")

    response = requests.delete(f"{BASE_URL}/orders/{order_id}")
    show_response(response)


def main_menu():
    """Menú principal"""
    while True:
        print()
        print("╔" + "═" * 48 + "╗")
        print("║" + " " * 10 + " ORM WORKSHOP CLIENT " + " " * 10 + "║")
        print("╚" + "═" * 48 + "╝")
        print()
        print("1. Crear cliente")
        print("2. Listar clientes")
        print("3. Crear producto")
        print("4. Listar productos")
        print("5. Crear orden desde JSON")
        print("6. Ver orden")
        print("7. Ver órdenes de cliente")
        print("8. Actualizar estado de orden")
        print("9. Eliminar orden")
        print("0. Salir")
        print()

        option = input("Opción: ").strip()

        if option == "1":
            create_customer()
        elif option == "2":
            list_customers()
        elif option == "3":
            create_product()
        elif option == "4":
            list_products()
        elif option == "5":
            create_order_from_json()
        elif option == "6":
            show_order()
        elif option == "7":
            show_customer_orders()
        elif option == "8":
            update_order_status()
        elif option == "9":
            delete_order()
        elif option == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    main_menu()