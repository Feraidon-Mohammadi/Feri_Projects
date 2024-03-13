class Device:
    count = 0

    def __init__(self, ip, mac, name):
        self.ip = ip
        self.mac = mac
        self.name = name

        # result = ping the device
        result = True
        if result:
            self.status = "active"
        else:
            self.status = "unknown"

    def get_status(self):
        return self.status  # return result  based on ping results for self.ip
