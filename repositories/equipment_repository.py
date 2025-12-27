from db import get_connection

class EquipmentRepository:

    def add(self, name, price):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO equipment (name, price) VALUES (%s, %s)",
            (name, price)
        )
        conn.commit()
        conn.close()

    def get_all(self):
        conn = get_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM equipment")
        data = cur.fetchall()
        conn.close()
        return data
