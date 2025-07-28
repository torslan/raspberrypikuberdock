#!/bin/bash
# Setup Docker and k3s on a Raspberry Pi
# Usage: run this script after SSH-ing into the Pi

set -euo pipefail

sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo systemctl enable docker
sudo usermod -aG docker "$USER"

# Install k3s (lightweight Kubernetes)
curl -sfL https://get.k3s.io | sh -

sudo kubectl get nodes

cat <<'INSTRUCTIONS'
If k3s fails to start with a cgroup v2 error, edit /boot/firmware/cmdline.txt
and add the following parameters at the end of the line:

cgroup_memory=1 cgroup_enable=memory systemd.unified_cgroup_hierarchy=1

Reboot and then run:
  sudo systemctl restart k3s
  sudo systemctl status k3s
INSTRUCTIONS
