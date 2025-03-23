import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from connect_db import get_connection
from datetime import datetime

def insert_reservation(user_id, parking_spot, reservation_time, duration_minutes, payment_id=None, status="active"):
    try:
        conn = get_connection()
        cur = conn.cursor()

        query = """
        INSERT INTO reservations (user_id, parking_spot, reservation_time, duration_minutes, payment_id, status)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cur.execute(query, (
            user_id,
            parking_spot,
            reservation_time,
            duration_minutes,
            payment_id,
            status
        ))

        conn.commit()
        cur.close()
        conn.close()
        print("✅ Réservation insérée avec succès.")
    except Exception as e:
        print("❌ Erreur lors de l'insertion de la réservation :", e)
