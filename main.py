from repositories.customer_repository import CustomerRepository
from repositories.car_repository import CarRepository
from repositories.equipment_repository import EquipmentRepository
from services.order_service import OrderService

customer_repo = CustomerRepository()
car_repo = CarRepository()
equipment_repo = EquipmentRepository()
order_service = OrderService()

def menu():
    print("1 - Přidat zákazníka")
    print("2 - Přidat auto")
    print("3 - Přidat výbavu")
    print("4 - Vytvořit objednávku")
    print("0 - Konec")

while True:
    menu()
    choice = input("Volba: ")

    if choice == "1":
        name = input("Jméno: ")
        email = input("Email: ")
        customer_repo.add(name, email)

    elif choice == "2":
        brand = input("Značka: ")
        model = input("Model: ")
        price = float(input("Cena: "))
        fuel = input("Palivo (petrol/diesel/electric): ")
        car_repo.add(brand, model, price, fuel)

    elif choice == "3":
        name = input("Název výbavy: ")
        price = float(input("Cena: "))
        equipment_repo.add(name, price)

    elif choice == "4":
        customer_id = int(input("ID zákazníka: "))
        eq_ids = input("ID výbavy (oddělené čárkou): ")
        equipment_ids = [int(x) for x in eq_ids.split(",")]
        order_id = order_service.create_order(customer_id, equipment_ids)
        print(f"Objednávka {order_id} vytvořena")

    elif choice == "0":
        break
