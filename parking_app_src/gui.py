import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from read_reservations import read_reservations
from make_reservation_with_payment import make_reservation_with_payment
from check_availability import update_expired_reservations
from pricing import calculate_price

# window
root = tk.Tk()
root.title("🚗 Parking App")
root.geometry("700x500")

# functions
def refresh_reservations(update_before=False):
    if update_before:
        update_expired_reservations()

    reservations_list.delete(0, tk.END)
    reservations = read_reservations()
    for res in reservations:
        line = f"{res.get('user_id')} | {res.get('parking_spot')} | {res.get('reservation_time')} | {res.get('status')}"
        reservations_list.insert(tk.END, line)

def open_add_window(parking_spot_value=None):
    def update_amount(*args):
        try:
            duration = int(entry_duration.get())
            amount = calculate_price(duration)
            amount_var.set(f"{amount:.2f}")
        except:
            amount_var.set("")

    def submit_reservation():
        user = "user_test_001"  # temporaire jusqu'à gestion des utilisateurs
        spot = entry_spot.get()
        date = entry_date.get()
        duration = entry_duration.get()
        amount = amount_var.get()
        method = method_var.get()

        try:
            reservation_time = datetime.strptime(date, "%Y-%m-%d %H:%M")
            duration_int = int(duration)
            amount_float = float(amount)

            reservation_id = make_reservation_with_payment(
                parking_spot=spot,
                reservation_time=reservation_time,
                duration_minutes=duration_int,
                amount=amount_float,
                method=method
            )

            if reservation_id:
                messagebox.showinfo("Success", "✅ Reservation and payment completed!")
                add_window.destroy()
                refresh_reservations()
            else:
                messagebox.showerror("Error", "❌ Reservation or payment failed.")

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid date, duration and amount.")
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong: {e}")

    add_window = tk.Toplevel(root)
    add_window.title("Add Reservation with Payment")

    tk.Label(add_window, text="Parking Spot:").pack()
    entry_spot = tk.Entry(add_window)
    entry_spot.pack()
    if parking_spot_value:
        entry_spot.insert(0, parking_spot_value)

    tk.Label(add_window, text="Date (YYYY-MM-DD HH:MM):").pack()
    entry_date = tk.Entry(add_window)
    entry_date.pack()
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry_date.insert(0, now_str)

    tk.Label(add_window, text="Duration (minutes):").pack()
    entry_duration = tk.Entry(add_window)
    entry_duration.pack()
    entry_duration.bind("<KeyRelease>", update_amount)

    tk.Label(add_window, text="Amount (€):").pack()
    amount_var = tk.StringVar()
    entry_amount = tk.Entry(add_window, textvariable=amount_var, state="readonly")
    entry_amount.pack()

    tk.Label(add_window, text="Payment Method:").pack()
    method_var = tk.StringVar(value="credit_card")
    tk.Entry(add_window, textvariable=method_var).pack()

    tk.Button(add_window, text="Submit", command=submit_reservation).pack(pady=10)

# ui elements

# title
tk.Label(root, text="📋 Reservations", font=("Helvetica", 16)).pack(pady=10)

# reservations lists
reservations_list = tk.Listbox(root, width=100)
reservations_list.pack(pady=10, fill=tk.BOTH, expand=True)

# control buttons
btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="🔄 Refresh Only", command=lambda: refresh_reservations()).pack(side=tk.LEFT, padx=10)
tk.Button(btn_frame, text="🔁 Refresh + Update", command=lambda: refresh_reservations(update_before=True)).pack(side=tk.LEFT, padx=10)
tk.Button(btn_frame, text="➕ Add Reservation + Payment", command=open_add_window).pack(side=tk.LEFT, padx=10)

# quick access
tk.Label(root, text="🅿️ Quick Access - Select a Parking Spot:").pack(pady=10)
map_frame = tk.Frame(root)
map_frame.pack()

for row in ["A", "B"]:
    for num in range(1, 3):
        spot = f"{row}{num}"
        tk.Button(map_frame, text=f"Place {spot}", width=12, command=lambda s=spot: open_add_window(s)).pack(side=tk.LEFT, padx=5, pady=5)

# launch
refresh_reservations()
root.mainloop()