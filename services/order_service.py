from db import get_connection

class OrderService:

    def create_order(self, customer_id: int, equipment_ids: list[int]):
        conn = get_connection()
        try:
            cur = conn.cursor()
            conn.start_transaction()

            cur.execute(
                "INSERT INTO car_order (customer_id, created_at, status) "
                "VALUES (%s, NOW(), 'new')",
                (customer_id,)
            )
            order_id = cur.lastrowid

            for eq_id in equipment_ids:
                cur.execute(
                    "INSERT INTO order_equipment (order_id, equipment_id) "
                    "VALUES (%s, %s)",
                    (order_id, eq_id)
                )

            conn.commit()
            return order_id

        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()
