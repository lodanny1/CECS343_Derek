import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from connect_db import get_connection


def insert_payment(user_id, amount, method, status, reservation_id):
    try:
        conn = get_connection()
        cur = conn.cursor()

        query = """
        INSERT INTO payments (user_id, amount, method, status, reservation_id)
        VALUES (%s, %s, %s, %s, %s)
        """
        cur.execute(query, (user_id, amount, method, status, reservation_id))

        conn.commit()
        cur.close()
        conn.close()
        print("✅ Paiement manuel inséré avec succès.")
    except Exception as e:
        print("❌ Erreur lors de l'insertion manuelle :", e)


def insert_payment_auto(user_id, amount, method, status, reservation_id):
    """
    Insère un paiement et retourne son ID.
    """
    try:
        conn = get_connection()
        cur = conn.cursor()

        query = """
        INSERT INTO payments (user_id, amount, method, status, reservation_id)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id
        """
        cur.execute(query, (user_id, amount, method, status, reservation_id))

        payment_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        print(f"✅ Paiement automatique créé (ID : {payment_id})")
        return payment_id
    except Exception as e:
        print("❌ Erreur lors de l'insertion automatique :", e)
        return None
