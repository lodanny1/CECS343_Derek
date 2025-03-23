from insert_payment import insert_payment, insert_payment_auto
from read_payments import read_all_payments
from create_table import create_payments_table

from insert_reservation import insert_reservation
from read_reservations import read_all_reservations
from create_reservations_table import create_reservations_table

from datetime import datetime

def menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Créer la table des paiements")
        print("2. Ajouter un paiement")
        print("3. Voir les paiements")
        print("4. Créer la table des réservations")
        print("5. Ajouter une réservation (avec paiement)")
        print("6. Voir les réservations")
        print("7. Quitter")

        choice = input("➡️ Choix : ")

        if choice == "1":
            create_payments_table()
        elif choice == "2":
            user = input("User ID : ")
            amount = float(input("Montant (€) : "))
            method = input("Méthode (credit_card/paypal...) : ")
            status = input("Statut (pending/completed) : ")
            res_id = input("Reservation ID : ")
            insert_payment(user, amount, method, status, res_id)
        elif choice == "3":
            read_all_payments()
        elif choice == "4":
            create_reservations_table()
        elif choice == "5":
            user = input("User ID : ")
            spot = input("Numéro de place : ")
            time_str = input("Date et heure (YYYY-MM-DD HH:MM) : ")
            try:
                time = datetime.strptime(time_str, "%Y-%m-%d %H:%M")
            except ValueError:
                print("❌ Format invalide. Ex : 2025-03-22 14:30")
                continue
            duration = int(input("Durée en minutes : "))
            status = input("Statut de la réservation (active/completed) : ")

            # 💰 Calcul montant automatique : 1€ / 30 min
            amount = round(duration / 30 * 1.00, 2)

            # Générer un reservation_id temporaire (utile pour relier les deux)
            fake_res_id = f"{user}_{spot}_{int(time.timestamp())}"

            # 🔁 Créer le paiement et récupérer son ID
            payment_id = insert_payment_auto(
                user_id=user,
                amount=amount,
                method="credit_card",
                status="pending",
                reservation_id=fake_res_id
            )

            # 🧾 Créer la réservation avec le payment_id
            insert_reservation(
                user_id=user,
                parking_spot=spot,
                reservation_time=time,
                duration_minutes=duration,
                payment_id=payment_id,
                status=status
            )

            print("✅ Réservation + paiement enregistrés avec succès.")
        elif choice == "6":
            read_all_reservations()
        elif choice == "7":
            print("👋 À bientôt !")
            break
        else:
            print("❌ Choix invalide.")

if __name__ == "__main__":
    menu()
