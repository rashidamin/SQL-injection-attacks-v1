# SDN Configuration Guide

## Requirements
- Mininet
- Ryu Controller
- OpenFlow 1.3

---

## Setup Steps

1. Start Mininet:
sudo mn --topo single,3 --controller remote

2. Run Controller:
ryu-manager sdn/controller.py

---

## Workflow

1. Traffic enters SDN network
2. Packets forwarded to controller
3. ML model predicts attack or benign
4. Controller applies flow rules

---

## Integration

CNN–KNN model → SDN Controller → Flow Rule Enforcement