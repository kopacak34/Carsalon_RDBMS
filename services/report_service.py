from db import get_connection
import mysql.connector

class ReportService:

    def order_totals(self):
        conn = get_connection()
        try:
            cur = conn.cursor(dictionary=True)
            cur.execute("SELECT * FROM v_order_total")
            return cur.fetchall()
        except mysql.connector.Error:
            print("Report nelze zobrazit – databázový pohled neexistuje.")
            return []
        finally:
            conn.close()
