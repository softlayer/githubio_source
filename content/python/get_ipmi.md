---
title: "Get IPMI info for BMS"
description: "Retrieve IPMI address, username, and password for all hardware on the account"
date: "2014-09-01"
classes:
  - "SoftLayer_Account"
tags:
  - "ipmi"
  - "dedicated"
  - "auth"
---

```python
import SoftLayer
from pprint import pprint as pp
 
client = SoftLayer.Client()
      
mask = """mask[networkManagementIpAddress,remoteManagementAccounts[username,password],id,fullyQualifiedDomainName]"""
         
result = client['SoftLayer_Account'].getHardware(mask=mask)
pp(result)
```
