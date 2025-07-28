#!/usr/bin/env python3

"""Simple Bluetooth connectivity test using PyBluez."""

import sys

try:
    import bluetooth
except ImportError:  # pragma: no cover - runtime dependency check
    print(
        "The 'bluetooth' module is required. Install it with 'pip install pybluez'.",
        file=sys.stderr,
    )
    sys.exit(1)

def scan_for_devices():
    print("Scanning for nearby Bluetooth devices...")
    nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True, lookup_class=False)

    if not nearby_devices:
        print("No devices found.")
    else:
        print(f"Found {len(nearby_devices)} devices.")
        for idx, device in enumerate(nearby_devices):
            address = device
            name = bluetooth.lookup_name(address)
            print(f"{idx + 1}: {name} ({address})")

    return nearby_devices

def connect_to_device(device_address: str):
    """Return an RFCOMM socket connected to ``device_address``."""

    print(f"Connecting to {device_address}...")
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((device_address, 1))
    return sock

def send_and_receive(sock):
    """Send a test message and print the response."""

    try:
        message = "Hello, Bluetooth device!"
        print(f"Sending message: {message}")
        sock.send(message)
        response = sock.recv(1024)
        print(f"Received response: {response}")
    finally:
        sock.close()

if __name__ == "__main__":
    devices = scan_for_devices()

    if devices:
        device_address = devices[0] # Use the first found device for testing
        sock = connect_to_device(device_address)
        send_and_receive(sock)
