# create_table.py

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from connect_db import get_connection

def create_payments_table():
    query = """
    CREATE TABLE IF NOT EXISTS payments (
        id SERIAL PRIMARY KEY,
        user_id VARCHAR(50) NOT NULL,
        amount DECIMAL(10, 2) NOT NULL,
        method VARCHAR(20),
        status VARCHAR(20),
        reservation_id VARCHAR(50),
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
        print("✅ Table 'payments' créée avec succès.")
    except Exception as e:
        print("❌ Erreur lors de la création :", e)

