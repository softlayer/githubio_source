---
title: "Create a virtual server from an existing image template"
description: "Provide an image template with a virtual machine order instead of
an OS"
date: "2014-09-01"
classes: ["SoftLayer_Product_Order"]
tags: ["virtual server", "ordering"]

---

```python
import SoftLayer
from pprint import pprint as pp

templateId = 12345

client = SoftLayer.Client()

order = {
    'complexType': 'SoftLayer_Container_Product_Order_Virtual_Guest',
    'quantity': 1,
    'virtualGuests': [
        {'hostname': 'test-template', 'domain': 'example.com'}
    ],
    'location': 168642,  # San Jose 1
    'packageId': 46,  # CCI Package
    'prices': [
        {'id': 1640},  # 1 x 2.0 GHz Core
        {'id': 1644},  # 1 GB RAM
        {'id':  905},  # Reboot / Remote Console
        {'id':  272},  # 10 Mbps Public & Private Networks
        {'id':50231},  # 1000 GB Bandwidth
        {'id':   21},  # 1 IP Address
        {'id': 2202},  # 25 GB (SAN)
        {'id': 1684},  # CentOS 5 - Minimal Install (32 bit)
        {'id':   55},  # Host Ping Monitoring
        {'id':   57},  # Email and Ticket Notifications
        {'id':   58},  # Automated Notification Response
        {'id':  420},  # Unlimited SSL VPN Users & 1 PPTP VPN User per account
        {'id':  418},  # Nessus Vulnerability Assessment & Reporting
    ],
    'imageTemplateId': templateId
}

result = client['SoftLayer_Product_Order'].verifyOrder(order)
pp(result)
```
