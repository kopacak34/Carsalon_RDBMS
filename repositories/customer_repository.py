from db import get_connection

class CustomerRepository:

    def add(self, name, email):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO customer (name, email, active) VALUES (%s, %s, TRUE)",
            (name, email)
        )
        conn.commit()
        conn.close()

    def get_all(self):
        conn = get_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM customer")
        data = cur.fetchall()
        conn.close()
        return data

    def delete(self, customer_id):
        conn = get_connection()
        cur = conn.cursor()
        try:
            cur.execute(
                "DELETE FROM customer WHERE id = %s",
                (customer_id,)
            )
            conn.commit()
            return cur.rowcount > 0
        except Exception as e:
            conn.rollback()
            print("Nelze smazat zákazníka:", e)
            return False
        finally:
            conn.close()

