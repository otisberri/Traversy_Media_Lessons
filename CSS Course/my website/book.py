class BookingSystem:
    def __init__(self):
        # Initialize an empty list to store bookings
        self.bookings = []

    def make_booking(self, name, date, time, duration):
        # Create a new booking and add it to the list of bookings
        booking = {
            'name': name,
            'date': date,
            'time': time,
            'duration': duration
        }
        self.bookings.append(booking)

    def get_bookings(self, date):
        # Return a list of bookings on the specified date
        return [b for b in self.bookings if b['date'] == date]

# Example usage
booking_system = BookingSystem()
booking_system.make_booking('Alice', '2022-01-01', '14:00', 2)
booking_system.make_booking('Bob', '2022-01-01', '16:00', 1)
booking_system.make_booking('Charlie', '2022-01-02', '10:00', 3)
print(booking_system.get_bookings('2022-01-01'))
# Output: [{'name': 'Alice', 'date': '2022-01-01', 'time': '14:00', 'duration': 2},
#          {'name': 'Bob', 'date': '2022-01-01', 'time': '16:00', 'duration': 1}]
print(booking_system.get_bookings('2022-01-02'))
# Output: [{'name': 'Charlie', 'date': '2022-01-02', 'time': '10:00', 'duration': 3}]
