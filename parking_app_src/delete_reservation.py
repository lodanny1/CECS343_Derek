from connect_mongo import get_mongo_collections
from bson.objectid import ObjectId

# Get collections
_, reservations_collection = get_mongo_collections()

def list_reservations():
    """
    Lists all reservations with an index to make deletion easier.
    """
    try:
        reservations = list(reservations_collection.find())
        print("\n--- Reservations ---")
        for i, res in enumerate(reservations):
            print(f"[{i}] {res.get('parking_spot')} | {res.get('reservation_time')} | {res.get('status')} | ID: {res.get('_id')}")
        return reservations
    except Exception as e:
        print("❌ Error while listing reservations:", e)
        return []

def delete_reservation_by_id(reservation_id):
    """
    Deletes a reservation by its MongoDB ObjectId.
    """
    try:
        result = reservations_collection.delete_one({"_id": ObjectId(reservation_id)})
        if result.deleted_count == 1:
            print(f"✅ Reservation {reservation_id} deleted successfully.")
        else:
            print(f"❌ No reservation found with ID: {reservation_id}")
    except Exception as e:
        print("❌ Error while deleting reservation:", e)

# Test interactif
if __name__ == "__main__":
    all_reservations = list_reservations()
    if all_reservations:
        try:
            index = int(input("\nEnter the index of the reservation to delete: "))
            selected_id = all_reservations[index]['_id']
            delete_reservation_by_id(selected_id)
        except (ValueError, IndexError):
            print("❌ Invalid index.")
    else:
        print("No reservations found.")