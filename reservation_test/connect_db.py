import psycopg2

DATABASE_URL = "postgresql://payment_c3ig_user:CEowrdi4GyedXtV0OxQWtBoTeGmpGuTB@dpg-cvf38152ng1s73d18uo0-a.oregon-postgres.render.com/payment_c3ig"

def get_connection():
    return psycopg2.connect(DATABASE_URL)
