from tv import TV
from termo import Thermo
from smart_tv import SmartTV


tv1 = TV("192.168.1.100", "00:11:22:33:44:55", "Living Room TV")
thermo1 = Thermo("192.168.1.200", "00:AA:BB:CC:DD:EE", "Living Room Thermostat")
smart_tv1 = SmartTV("192.168.1.101", "00:11:22:33:44:56", "Smart TV")

print(tv1.get_status())
tv1.turn_on()
tv1.turn_off()

print(thermo1.get_status())
print(thermo1.get_degree())

smart_tv1.turn_on()
smart_tv1.turn_off()
