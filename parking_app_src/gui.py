import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from insert_reservations import insert_reservation
from read_reservations import read_reservations
from check_availability import is_spot_available, update_expired_reservations

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
    def submit_reservation():
        user = entry_user.get()
        spot = entry_spot.get()
        date = entry_date.get()
        duration = entry_duration.get()
        status = status_var.get()

        try:
            reservation_time = datetime.strptime(date, "%Y-%m-%d %H:%M")
            duration_int = int(duration)

            # check availability
            if not is_spot_available(spot, reservation_time, duration_int):
                messagebox.showerror("Unavailable", f"Spot {spot} is already taken at this time.")
                return

            insert_reservation(user, spot, reservation_time, duration_int, status=status)
            messagebox.showinfo("Success", "Reservation added!")
            add_window.destroy()
            refresh_reservations()

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid date and duration.")
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong: {e}")

    add_window = tk.Toplevel(root)
    add_window.title("Add Reservation")

    tk.Label(add_window, text="User ID:").pack()
    entry_user = tk.Entry(add_window)
    entry_user.pack()

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

    tk.Label(add_window, text="Status:").pack()
    status_var = tk.StringVar(value="active")
    tk.Entry(add_window, textvariable=status_var).pack()

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
tk.Button(btn_frame, text="➕ Add manually", command=open_add_window).pack(side=tk.LEFT, padx=10)

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