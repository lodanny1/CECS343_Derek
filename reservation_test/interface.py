import tkinter as tk
from tkinter import messagebox
from datetime import datetime

from insert_reservation import insert_reservation
from insert_payment import insert_payment_auto
from read_reservations import read_all_reservations
from read_payments import read_all_payments


def ajouter_reservation():
    def valider():
        user = entry_user.get()
        spot = entry_spot.get()
        time_str = entry_time.get()
        duration = entry_duration.get()
        status = entry_status.get()

        try:
            time = datetime.strptime(time_str, "%Y-%m-%d %H:%M")
            duration = int(duration)
        except:
            messagebox.showerror("Erreur", "Format de date ou durée invalide.")
            return

        amount = round(duration / 30 * 1.00, 2)
        fake_res_id = f"{user}_{spot}_{int(time.timestamp())}"

        payment_id = insert_payment_auto(user, amount, "credit_card", "pending", fake_res_id)
        insert_reservation(user, spot, time, duration, payment_id, status)

        messagebox.showinfo("Succès", "Réservation + paiement enregistrés avec succès.")
        fenetre.destroy()

    fenetre = tk.Toplevel(root)
    fenetre.title("Nouvelle Réservation")

    tk.Label(fenetre, text="User ID").pack()
    entry_user = tk.Entry(fenetre)
    entry_user.pack()

    tk.Label(fenetre, text="Place").pack()
    entry_spot = tk.Entry(fenetre)
    entry_spot.pack()

    tk.Label(fenetre, text="Date (YYYY-MM-DD HH:MM)").pack()
    entry_time = tk.Entry(fenetre)
    entry_time.pack()

    tk.Label(fenetre, text="Durée (minutes)").pack()
    entry_duration = tk.Entry(fenetre)
    entry_duration.pack()

    tk.Label(fenetre, text="Statut").pack()
    entry_status = tk.Entry(fenetre)
    entry_status.insert(0, "active")
    entry_status.pack()

    tk.Button(fenetre, text="Valider", command=valider).pack(pady=10)


def voir_reservations():
    read_all_reservations()


def voir_paiements():
    read_all_payments()


# Interface principale
root = tk.Tk()
root.title("Interface Réservation & Paiement")

tk.Button(root, text="➕ Ajouter une réservation", width=30, command=ajouter_reservation).pack(pady=10)
tk.Button(root, text="📋 Voir les réservations", width=30, command=voir_reservations).pack(pady=10)
tk.Button(root, text="💸 Voir les paiements", width=30, command=voir_paiements).pack(pady=10)

root.mainloop()
