from repositories.customer_repository import CustomerRepository
from repositories.car_repository import CarRepository
from repositories.equipment_repository import EquipmentRepository
from services.order_service import OrderService
from services.import_service import ImportService
from services.report_service import ReportService

customer_repo = CustomerRepository()
car_repo = CarRepository()
equipment_repo = EquipmentRepository()
order_service = OrderService()
import_service = ImportService()
report_service = ReportService()

def menu():
    print("\n--- AUTOSALON ---")
    print("1 - Přidat zákazníka")
    print("2 - Přidat auto")
    print("3 - Přidat výbavu")
    print("4 - Vytvořit objednávku")
    print("5 - Import dat")
    print("6 - Report objednávek")
    print("7 - Smazat zákazníka")
    print("8 - Smazat auto")
    print("0 - Konec")

while True:
    menu()
    volba = input("Volba: ")

    try:
        if volba == "1":
            customer_repo.add(input("Jméno: "), input("Email: "))

        elif volba == "2":
            car_repo.add(
                input("Značka: "),
                input("Model: "),
                float(input("Cena: ")),
                input("Palivo (petrol/diesel/electric): ")
            )

        elif volba == "3":
            equipment_repo.add(input("Název: "), float(input("Cena: ")))

        elif volba == "4":
            cid = int(input("ID zákazníka: "))
            eq = input("ID výbavy (1,2,3): ")
            order_id = order_service.create_order(cid, [int(x) for x in eq.split(",")])
            print("Objednávka vytvořena:", order_id)

        elif volba == "5":
            import_service.import_customers_csv("data/customers.csv")
            import_service.import_cars_json("data/cars.json")
            print("Import hotov")

        elif volba == "6":
            for r in report_service.order_totals():
                print(r)

        elif volba == "7":
            customer_id = int(input("ID zákazníka ke smazání: "))
            if customer_repo.delete(customer_id):
                print("Zákazník smazán")
            else:
                print("Zákazníka nelze smazat")

        elif volba == "8":
            car_id = int(input("ID auta ke smazání: "))
            if car_repo.delete(car_id):
                print("Auto smazáno")
            else:
                print("Auto nelze smazat")

        elif volba == "0":
            break

    except Exception as e:
        print("Chyba:", e)
