from devices import Device


class Thermo(Device):
    def get_degree(self):
        # Implement the logic to get the temperature reading from self.ip
        print(f"Reading temperature from {self.ip}")
        return 25  # Replace this with the actual temperature reading
