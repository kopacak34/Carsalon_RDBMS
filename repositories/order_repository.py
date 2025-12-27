from db import get_connection

class OrderRepository:

    def create(self, customer_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO car_order (customer_id, created_at, status) VALUES (%s, NOW(), 'new')",
            (customer_id,)
        )
        order_id = cur.lastrowid
        conn.commit()
        conn.close()
        return order_id
