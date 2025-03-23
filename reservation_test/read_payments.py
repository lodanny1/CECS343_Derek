import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from connect_db import get_connection

def read_all_payments():
    try:
        conn = get_connection()
        cur = conn.cursor()

        query = "SELECT * FROM payments ORDER BY created_at DESC"
        cur.execute(query)

        rows = cur.fetchall()

        if rows:
            print("📄 Paiements enregistrés :\n")
            for row in rows:
                print(f"ID: {row[0]} | User: {row[1]} | Amount: {row[2]}€ | Method: {row[3]} | Status: {row[4]} | Reservation: {row[5]} | Date: {row[6]}")
        else:
            print("⚠️ Aucun paiement trouvé.")

        cur.close()
        conn.close()
    except Exception as e:
        print("❌ Erreur lors de la lecture :", e)

