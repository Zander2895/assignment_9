# Task 1: Formatting Flight Itineraries Create a Python function that takes a list of tuples as an argument.
# Each tuple contains information about a flight itinerary: (traveler_name, origin, destination).
# The function should format and return a string that lists each itinerary.
# For example, if the input is `[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]`,
# the output should be a string formatted as:

# "Itinerary 1: Alice - From New York to London
#  Itinerary 2: Bob - From Tokyo to San Francisco"

def itinerary(traveler_name, origin, destination):
    return f"{traveler_name} - From {origin} to {destination}"
traveler_name = input("What's your name? ")
origin = input("Where are you traveling from? ")
destination = input("Where are you headed? ")
print(itinerary (traveler_name, origin, destination))
    

