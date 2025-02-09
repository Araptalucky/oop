class Hotel:
    def __init__(self):
        self.rooms = {101: "Available", 102: "Available", 103: "Available"}  # Room status

    def book_room(self, room_number):
        if room_number in self.rooms and self.rooms[room_number] == "Available":
            self.rooms[room_number] = "Booked"
            print(f"Room {room_number} has been booked successfully!")
        else:
            print(f"Room {room_number} is either not available or does not exist.")

    def checkout(self, room_number):
        if room_number in self.rooms and self.rooms[room_number] == "Booked":
            self.rooms[room_number] = "Available"
            print(f"Room {room_number} has been checked out successfully!")
        else:
            print(f"Room {room_number} is not booked or does not exist.")

    def display_rooms(self):
        print("\nRoom Status:")
        for room, status in self.rooms.items():
            print(f"Room {room}: {status}")

# Example usage
hotel = Hotel()
hotel.display_rooms()
hotel.book_room(101)
hotel.display_rooms()
hotel.checkout(101)
hotel.display_rooms()
