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

    class CarRepository:

        def delete(self, car_id):
            conn = get_connection()
            cur = conn.cursor()
            try:
                cur.execute(
                    "DELETE FROM car WHERE id = %s",
                    (car_id,)
                )
                conn.commit()
                return cur.rowcount > 0
            except Exception as e:
                conn.rollback()
                print("Nelze smazat auto:", e)
                return False
            finally:
                conn.close()

