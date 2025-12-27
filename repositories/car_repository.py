from db import get_connection

class CarRepository:

    def add(self, brand, model, price, fuel):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO car (brand, model, price, fuel, available) VALUES (%s, %s, %s, %s, TRUE)",
            (brand, model, price, fuel)
        )
        conn.commit()
        conn.close()

    def get_available(self):
        conn = get_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM car WHERE available = TRUE")
        cars = cur.fetchall()
        conn.close()
        return cars
