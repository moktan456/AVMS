# Autonomous Vehicle Management System (AVMS)
# AVMS.py
import numpy as np
from heap import HEAP
from hash import DSAHashTable
from graph import DSAGraph, Stack, Queue, SinglyLinkedList

# Vehicle Class Definition


class Vehicle:
    def __init__(self, vehicle_id, location, destination, distance_to_destination, battery_level):
        self.vehicle_id = vehicle_id
        self.location = location
        self.destination = destination
        self.distance_to_destination = distance_to_destination
        self.battery_level = battery_level

    def setLocation(self, location):
        self.location = location

    def setDestination(self, destination):
        self.destination = destination

    def setDistanceToDestination(self, distance):
        self.distance_to_destination = distance

    def setBatteryLevel(self, level):
        self.battery_level = level

    def getLocation(self):
        return self.location

    def getDestination(self):
        return self.destination

    def getDistanceToDestination(self):
        return self.distance_to_destination

    def getBatteryLevel(self):
        return self.battery_level

    def __str__(self):
        return (f"Vehicle ID: {self.vehicle_id}, Location: {self.location}, "
                f"Destination: {self.destination}, Distance to Destination: {
                    self.distance_to_destination}, "
                f"Battery Level: {self.battery_level}%")

# VehicleHashTable Class using DSAHashTable


class VehicleHashTable(DSAHashTable):
    def __init__(self, size):
        super().__init__(size)

    def add_vehicle(self, vehicle):
        self.put(vehicle.vehicle_id, vehicle)

    def remove_vehicle(self, vehicle_id):
        self.remove(vehicle_id)

    def get_vehicle(self, vehicle_id):
        return self.get(vehicle_id)

    def display_all_vehicles(self):
        self.display()

# Sorting Functions (implemented using quicksort algorithm)


def quicksort_vehicles_by_battery(vehicles):
    if len(vehicles) <= 1:
        return vehicles
    pivot = vehicles[len(vehicles) // 2]
    left = [v for v in vehicles if v.battery_level > pivot.battery_level]
    middle = [v for v in vehicles if v.battery_level == pivot.battery_level]
    right = [v for v in vehicles if v.battery_level < pivot.battery_level]
    return quicksort_vehicles_by_battery(left) + middle + quicksort_vehicles_by_battery(right)


def find_vehicle_with_highest_battery(vehicles):
    sorted_vehicles = quicksort_vehicles_by_battery(vehicles)
    return sorted_vehicles[0]  # Vehicle with the highest battery level


def find_nearest_vehicle(vehicles):
    """Find the vehicle that is closest to its destination based on distance_to_destination."""
    if not vehicles:
        return None  # No vehicles available

    # Start with the first vehicle as the nearest
    nearest_vehicle = vehicles[0]
    for vehicle in vehicles:
        if vehicle.getDistanceToDestination() < nearest_vehicle.getDistanceToDestination():
            nearest_vehicle = vehicle  # Update if we find a closer vehicle
    return nearest_vehicle


def search_vehicle(vehicle_hash_table):
    """Search for a specific vehicle in the hash table using its vehicle ID."""
    vehicle_id = input("Enter the Vehicle ID to search: ")
    try:
        vehicle = vehicle_hash_table.get_vehicle(vehicle_id)
        if vehicle:
            print(f"Vehicle found: {vehicle}")
        else:
            print(f"Vehicle with ID '{vehicle_id}' not found.")
    except KeyError:
        print(f"Vehicle with ID '{vehicle_id}' does not exist in the system.")

# Function to Load Vehicles from a File and add locations to the graph


def load_vehicles_from_file(file_path, vehicle_hash_table, vehicle_heap, vehicles, road_graph):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) == 5:
                    vehicle_id, location, destination, distance, battery = data
                    distance = float(distance)
                    battery = float(battery)
                    vehicle = Vehicle(vehicle_id, location,
                                      destination, distance, battery)
                    vehicle_hash_table.add_vehicle(vehicle)
                    vehicle_heap.add(distance, vehicle)
                    vehicles.append(vehicle)

                    # Add locations to the graph and connect them as edges
                    if not road_graph.hasVertex(location):
                        road_graph.addVertex(location)
                    if not road_graph.hasVertex(destination):
                        road_graph.addVertex(destination)
                    road_graph.addEdges(location, destination)

            print(
                "Vehicles loaded successfully from file and locations added to the graph.")
    except FileNotFoundError:
        print(
            f"File '{file_path}' not found. Please check the file path and try again.")
    except Exception as e:
        print(f"Error loading vehicles from file: {e}")

# Interactive Menu Implementation


def main_menu():
    vehicle_hash_table = VehicleHashTable(100)  # Initial hash table size
    vehicle_heap = HEAP(100)  # Max size for the heap
    road_graph = DSAGraph()  # Using the custom DSAGraph from graph.py
    vehicles = []  # List to keep track of vehicles for quicksort

    while True:
        print("\nAutonomous Vehicle Management System")
        print("1. Add Vehicle")
        print("2. Remove Vehicle")
        print("3. Display All Vehicles")
        print("4. Add Road Location (Graph Vertex)")
        print("5. Connect Locations (Graph Edge)")
        print("6. Display Road Network as List")
        print("7. Display Road Network as Matrix")
        print("8. Display Graph Structure")
        print("9. Get Neighboring Locations of a Location")
        print("10. Sort Vehicles by Distance to Destination (Heapsort)")
        print("11. Find Vehicle Closest to Destination")
        print("12. Sort Vehicles by Battery Level (Quicksort)")
        print("13. Find Vehicle with Highest Battery Level")
        print("14. Search Vehicle by ID")
        print("15. Load Vehicles from File")
        print("16. Exit")

        choice = input("Enter your choice (1-16): ")

        if choice == '1':
            vehicle_id = input("Enter Vehicle ID: ")
            location = input("Enter Current Location: ")
            destination = input("Enter Destination: ")
            distance_to_destination = float(
                input("Enter Distance to Destination: "))
            battery_level = float(input("Enter Battery Level (%): "))
            vehicle = Vehicle(vehicle_id, location, destination,
                              distance_to_destination, battery_level)
            vehicle_hash_table.add_vehicle(vehicle)
            vehicle_heap.add(distance_to_destination, vehicle)
            vehicles.append(vehicle)

            # Add locations to the graph and connect them as edges
            if not road_graph.hasVertex(location):
                road_graph.addVertex(location)
            if not road_graph.hasVertex(destination):
                road_graph.addVertex(destination)
            road_graph.addEdges(location, destination)

            print(f"Vehicle {vehicle_id} added successfully.")

        elif choice == '2':
            vehicle_id = input("Enter Vehicle ID to remove: ")
            vehicle_hash_table.remove_vehicle(vehicle_id)
            print(f"Vehicle {vehicle_id} removed from the system.")

        elif choice == '3':
            vehicle_hash_table.display_all_vehicles()

        elif choice == '4':
            location = input("Enter Location Name to Add: ")
            road_graph.addVertex(location)
            print(f"Location {location} added to the road network.")

        elif choice == '5':
            location1 = input("Enter Starting Location: ")
            location2 = input("Enter Destination Location: ")
            road_graph.addEdges(location1, location2)
            print(f"Edge added between {location1} and {location2}.")

        elif choice == '6':
            print("Displaying Road Network as List:")
            road_graph.displayAsList()

        elif choice == '7':
            print("Displaying Road Network as Matrix:")
            road_graph.displayAsMatrix()

        elif choice == '8':
            road_graph.displayGraph()

        elif choice == '9':
            location = input("Enter the location to find its neighbors: ")
            neighbors = road_graph.getNeighbors(location)
            print(f"Neighbors of {location}: {neighbors}")

        elif choice == '10':
            sorted_vehicles = vehicle_heap.heap_sort()
            print("\nVehicles sorted by distance to destination (Heapsort):")
            for vehicle in sorted_vehicles:
                print(vehicle)

        elif choice == '11':
            nearest_vehicle = find_nearest_vehicle(vehicles)
            if nearest_vehicle:
                print(f"The nearest vehicle to its destination is: {
                      nearest_vehicle}")
            else:
                print("No vehicles available to find the nearest.")

        elif choice == '12':
            sorted_vehicles = quicksort_vehicles_by_battery(vehicles)
            print("\nVehicles sorted by battery level (Quicksort):")
            for vehicle in sorted_vehicles:
                print(vehicle)

        elif choice == '13':
            highest_battery_vehicle = find_vehicle_with_highest_battery(
                vehicles)
            print(f"Vehicle with the highest battery level: {
                  highest_battery_vehicle}")

        elif choice == '14':
            search_vehicle(vehicle_hash_table)

        elif choice == '15':
            file_path = input(
                "Enter the file path to load vehicles (e.g., vehicles.txt): ")
            load_vehicles_from_file(
                file_path, vehicle_hash_table, vehicle_heap, vehicles, road_graph)

        elif choice == '16':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 16.")


if __name__ == "__main__":
    main_menu()
