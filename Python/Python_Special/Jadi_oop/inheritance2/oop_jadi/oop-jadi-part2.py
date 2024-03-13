def cleanup():
    Computer.count -= 1


class Computer:
    count = 0

    def __init__(self, **kw):
        Computer.count += 1
        self.color = kw.get("color")
        self.name = kw.get("name")
        self.types = kw.get("types")
        self.ram = kw.get("ram", 0)
        self.hdd = kw.get("hdd", 0)
        self.cpu = kw.get("cpu", 0)

    def value(self):
        return (f"\nPcType: {self.types}, PcName: {self.name}, "
                f"PcColor: {self.color}, Ram: {self.ram}, Hard Ware: {self.hdd}, CPU: {self.cpu}")

    # def cleanup(self):
    # Computer.count -= 1

    # or this del to remove
    def __del__(self):
        Computer.count -= 1


class Laptop(Computer):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = kwargs.get("size", 0)
        self.model = kwargs.get("model", 0)

    def value(self):
        computer_value = super().value()
        return f"{computer_value}, Size={self.size} Model={self.model}"


class HardWare(Laptop):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ssd = kwargs.get("ssd", 0)
        self.pci = kwargs.get("pci", 0)
        self.price = kwargs.get("price", 0)

    def value(self):
        laptop1_value = super().value()
        return f"{laptop1_value}, SSD:{self.ssd}, PCI:{self.pci}, price: {self.price}"


class Prices(Computer):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ram_price = kwargs.get("ram_price", 0)
        self.hdd_price = kwargs.get("hdd_price", 0)
        self.ssd_price = kwargs.get("ssd_price", 0)
        self.pc_price = kwargs.get("pc_price", 0)
        self.laptop_price = kwargs.get("laptop_price", 0)
        self.quantumPC_price = kwargs.get("quantumPC_price", 0)

    def value(self):
        computer_prices = super().value()

        return (f"{computer_prices}€ \n"
                f"Ram Price: {self.ram_price}€ \n"
                f"HDD_Price: {self.hdd_price}€ \n"
                f"SSD Price: {self.ssd_price}€ \n"
                f"Laptop Price: {self.laptop_price}€ \n"
                f"Quantum PC Price: {self.quantumPC_price}€ \n"
                )


prices = Prices(pc_price=950, ram_price=220, hdd_price=150, ssd_price=80, laptop_price=1459, quantumPC_price=200_000)
print(prices.value())


laptop1 = Laptop(color="red", name="del", types="iBook", ram=4, cpu=2, hdd=4, size=22, model="lenovo")
print(laptop1.value())

pc1 = Computer(color="green", name="hp", types="Quantum", ram=1024, cpu=64, hdd=6)
print(pc1.value())
del laptop1

pc2 = Computer(color="blue", name="asus", types="desktop", ram=6, cpu=4, hdd=4)
print(pc2.value())
cleanup()

laptop1_hardware = HardWare(ssd=3, pci=4, price=220)
print(laptop1_hardware.value())
