import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from connect_db import get_connection

def create_reservations_table():
    query = """
    CREATE TABLE IF NOT EXISTS reservations (
        id SERIAL PRIMARY KEY,
        user_id VARCHAR(50) NOT NULL,
        parking_spot VARCHAR(20),
        reservation_time TIMESTAMP,
        duration_minutes INTEGER,
        payment_id INTEGER REFERENCES payments(id) ON DELETE SET NULL,
        status VARCHAR(20),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        cur.close()
        conn.close()
        print("✅ Table 'reservations' créée avec succès.")
    except Exception as e:
        print("❌ Erreur lors de la création :", e)
