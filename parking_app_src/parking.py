"""
Manages the parking spots including displaying available spots and reserving a spot.
"""

from datetime import datetime

# Simulated parking spots database.
PARKING_SPOTS = [
    {"id": 1, "location": "Lot A", "available": True},
    {"id": 2, "location": "Lot B", "available": True},
    {"id": 3, "location": "Lot C", "available": False},  # Already reserved.
]

def get_available_spots():
    """
    Retrieves a list of available parking spots.

    Flow of Control:
        - The user selects the option to view available spots.
        - The system queries for and displays available spots.

    Returns:
        list: A list of dictionaries representing available parking spots.
    """
    return [spot for spot in PARKING_SPOTS if spot["available"]]

def reserve_spot(spot_id: int, user_id: str, time_slot: str) -> dict:
    """
    Reserves a parking spot if it is available.

    Flow of Control:
        - The user navigates to the reservation page.
        - The user selects a preferred time slot and spot.
        - The system checks the spot's availability and reserves it.
    
    Args:
        spot_id (int): The ID of the parking spot to reserve.
        user_id (str): The identifier of the user making the reservation.
        time_slot (str): The chosen time slot for the reservation.

    Returns:
        dict: Reservation details including time and spot information.

    Raises:
        ValueError: If the selected spot is unavailable or not found.
    """
    for spot in PARKING_SPOTS:
        if spot["id"] == spot_id:
            if spot["available"]:
                spot["available"] = False  # Reserve the spot.
                reservation = {
                    "user_id": user_id,
                    "spot_id": spot_id,
                    "time_slot": time_slot,
                    "reservation_time": datetime.now().isoformat()
                }
                # In a full application, reservation data would be persisted.
                return reservation
            else:
                raise ValueError("Selected Parking Spot is not available.")
    raise ValueError("Parking Spot not found.")
