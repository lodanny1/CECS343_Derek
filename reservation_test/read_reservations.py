import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from connect_db import get_connection

def read_all_reservations():
    try:
        conn = get_connection()
        cur = conn.cursor()

        query = "SELECT * FROM reservations ORDER BY reservation_time DESC"
        cur.execute(query)
        rows = cur.fetchall()

        if rows:
            print("📋 Réservations enregistrées :\n")
            for row in rows:
                print(f"ID: {row[0]} | User: {row[1]} | Spot: {row[2]} | Time: {row[3]} | Duration: {row[4]} min | Payment ID: {row[5]} | Status: {row[6]} | Created at: {row[7]}")
        else:
            print("⚠️ Aucune réservation trouvée.")

        cur.close()
        conn.close()
    except Exception as e:
        print("❌ Erreur lors de la lecture des réservations :", e)
