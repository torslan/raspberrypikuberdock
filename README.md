# Raspberry Pi Kubernetes + Docker Setup

This repository contains a small collection of scripts for configuring a
headless Raspberry Pi with Docker and the lightweight Kubernetes
distribution [k3s](https://k3s.io). It also includes a simple Python
script for testing Bluetooth connectivity.

## Usage

After connecting to your Raspberry Pi over SSH, run the setup script:

```bash
./setup_raspberrypi.sh
```

This installs Docker and k3s. If k3s fails to start due to cgroup
settings, follow the instructions printed at the end of the script.

The `v1_bluetooth_test.py` file demonstrates scanning for and connecting
to Bluetooth devices using the `pybluez` library.
