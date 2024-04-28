class TrafficSignalController:
    def __init__(self):
        self.green_time = 30  # Initial green time in seconds
        self.red_time = 20    # Initial red time in seconds
        self.yellow_time = 5  # Initial yellow time in seconds
        self.max_green_time = 60  # Maximum green time
        self.min_green_time = 10  # Minimum green time
        self.max_red_time = 40    # Maximum red time
        self.min_red_time = 10    # Minimum red time
        self.max_yellow_time = 10  # Maximum yellow time
        self.min_yellow_time = 3   # Minimum yellow time

    def update_signal_timings(self, vehicle_count):
        # Adjust green signal time based on vehicle count
        if vehicle_count > 50:
            self.green_time = min(self.green_time + 5, self.max_green_time)
        elif vehicle_count < 10:
            self.green_time = max(self.green_time - 5, self.min_green_time)
        
        # Adjust red signal time based on vehicle count
        if vehicle_count > 30:
            self.red_time = min(self.red_time + 5, self.max_red_time)
        elif vehicle_count < 20:
            self.red_time = max(self.red_time - 5, self.min_red_time)
        
        # Adjust yellow signal time based on other factors
        if vehicle_count > 30:
            self.yellow_time = min(self.yellow_time + 1, self.max_yellow_time)
        elif vehicle_count < 20:
            self.yellow_time = max(self.yellow_time - 1, self.min_yellow_time)

    def print_signal_timings(self):
        print("Green Signal Time:", self.green_time, "seconds")
        print("Red Signal Time:", self.red_time, "seconds")
        print("Yellow Signal Time:", self.yellow_time, "seconds")

def main():
    # Initialize Traffic Signal Controller
    signal_controller = TrafficSignalController()

    # Get vehicle count from user
    try:
        vehicle_count = int(input("Enter the vehicle count: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer for vehicle count.")
        return

    # Update signal timings based on vehicle count
    signal_controller.update_signal_timings(vehicle_count)

    # Print updated signal timings
    signal_controller.print_signal_timings()

if __name__ == "__main__":
    main()