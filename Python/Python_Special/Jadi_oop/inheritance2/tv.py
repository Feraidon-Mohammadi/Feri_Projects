from devices import Device


class TV(Device):
    def turn_on(self):
        # connect to self.ip and turn on
        print(f"Turning on the TV at {self.ip}")

    def turn_off(self):
        # connect to self.ip and turn off
        print(f"Turning off the TV at {self.ip}")
