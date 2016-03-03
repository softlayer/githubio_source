---
title: "Update Firmware on a Bare Metal Server"
description: "Create a firmware update transaction for the IPMI, BIOS, Hard Drives, or Raid Controller on your Bare Metal Server "
date: "2016-03-03"
classes: ["SoftLayer_Hardware_Server"]
tags:
    - "firmware"
---

In the following example we are updating the firmware for the IPMI, BIOS, Hard Drives, and Raid Controller on our Bare Metal Server with ID 12345. We can toggle the specific items we want updated by setting the values to False (Do not update firmware) or True (Do update firmware).

```python

import SoftLayer
client = SoftLayer.Client()
mgr = SoftLayer.HardwareManager(client)

result = mgr.update_firmware(hardware_id=12345,ipmi=True,raid_controller=True,bios=True,hard_drive=True)
```
