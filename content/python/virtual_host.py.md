---
title: "Virtual_host.py"
description: "Virtual_host.py"

date: "2019-07-27"
classes: 
    - "SoftLayer_Virtual_Host"    
    - "SoftLayer_Product_Order"    
tags:
    - "Virtual_host"
---

### getAccount

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
virtual_service = client['SoftLayer_Virtual_Host']

""""
Virtual host id variable. 
"""""
id_host="123456"

try:
    response = virtual_service.getAccount(id=id_host)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
  
```

### getBilledPerMemoryUsageFlag

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
virtual_service = client['SoftLayer_Virtual_Host']

""""
Virtual host id variable. 
"""""
id_host="123456"

try:
    response = virtual_service.getBilledPerMemoryUsageFlag(id=id_host)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```

### getGuests

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
virtual_service = client['SoftLayer_Virtual_Host']

""""
Virtual host id variable. 
"""""
id_host="123456"

try:
    response = virtual_service.getGuests(id=id_host)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### getHardware

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
virtual_service = client['SoftLayer_Virtual_Host']

""""
Virtual host id variable. 
"""""
id_host="123456"

try:
    response = virtual_service.getHardware(id=id_host)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
```
### getLiveGuestByUuid

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
virtual_service = client['SoftLayer_Virtual_Host']

""""
Virtual host id and uuid variable. 
"""""
id_host="1001547"
uuid="123456789-bb9a-fe82-7239-4a33077cf32f"
try:
    response = virtual_service.getLiveGuestByUuid(uuid,id=id_host)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### getLiveGuestList
```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
virtual_service = client['SoftLayer_Virtual_Host']

""""
Virtual host id variable. 
"""""
id_host = "123456"
try:
    response = virtual_service.getLiveGuestList(id=id)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### getLiveGuestRecentMetricData

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
virtual_service = client['SoftLayer_Virtual_Host']

""""
Virtual host id and uuid variable. 
"""""
id_host="1001547"
uuid="123456789-bb9a-fe82-7239-4a33077cf32f"
try:
    response = virtual_service.getLiveGuestRecentMetricData(uuid,id=id_host)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### getLiveGuestRecentMetricData

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
virtual_service = client['SoftLayer_Virtual_Host']

""""
Virtual host id variable. 
"""""

id_host="123456"

try:
    response = virtual_service.getMetricTrackingObject(id=id_host)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### getObject

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
virtual_service = client['SoftLayer_Virtual_Host']

""""
Virtual host id variable. 
"""""

id_host="123456"

try:
    response = virtual_service.getObject(id=id_host)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### getPciDevices

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
virtual_service = client['SoftLayer_Virtual_Host']

""""
Virtual host id variable. 
"""""

id_host="123456"

try:
    response = virtual_service.getPciDevices(id=id_host)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### pauseLiveGuest

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
virtual_service = client['SoftLayer_Virtual_Host']

""""
Virtual host id and uuid variable. 
"""""
id_host="1001547"
uuid="12345678-bb9a-fe82-7239-4a33077cf32f"

try:
    response = virtual_service.pauseLiveGuest(uuid,id=id_host)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
```


### powerCycleLiveGuest

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
virtual_service = client['SoftLayer_Virtual_Host']

""""
Virtual host id and uuid variable. 
"""""
id_host="1001547"
uuid="12345678-bb9a-fe82-7239-4a33077cf32f"

try:
    response = virtual_service.powerCycleLiveGuest(uuid,id=id_host)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### powerOffLiveGuest

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
virtual_service = client['SoftLayer_Virtual_Host']

""""
Virtual host id and uuid variable. 
"""""
id_host="1001547"
uuid="12345678-bb9a-fe82-7239-4a33077cf32f"

try:
    response = virtual_service.powerOffLiveGuest(uuid,id=id_host)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### powerOnLiveGuest

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
virtual_service = client['SoftLayer_Virtual_Host']

""""
Virtual host id and uuid variable. 
"""""
id_host="1001547"
uuid="12345678-bb9a-fe82-7239-4a33077cf32f"

try:
    response = virtual_service.powerOnLiveGuest(uuid,id=id_host)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### rebootSoftLiveGuest

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
virtual_service = client['SoftLayer_Virtual_Host']

""""
Virtual host id and uuid variable. 
"""""
id_host="1001547"
uuid="12345678-bb9a-fe82-7239-4a33077cf32f"

try:
    response = virtual_service.rebootSoftLiveGuest(uuid,id=id_host)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### resumeLiveGuest

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
virtual_service = client['SoftLayer_Virtual_Host']

""""
Virtual host id and uuid variable. 
"""""
id_host="1001547"
uuid="12345678-bb9a-fe82-7239-4a33077cf32f"

try:
    response = virtual_service.resumeLiveGuest(uuid,id=id_host)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
```


### Create virtual host

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
apiAuthenticationKey = client['SoftLayer_Product_Order']

body_json = {
    "complexType": "SoftLayer_Container_Product_Order",
    "extendedHardwareTesting": True,
    "hardware": [
        {
            "domain": "testAPISuport",
            "hostname": "baremetalnew"
        }
    ],
    "location": "448994",
    "packageId": 1051,
    "prices": [
        {"id": 202483}, #INTEL_INTEL_XEON_4110_2_10
        {"id": 209393}, #RAM_32_GB_DDR4_2133_ECC_NON_REG
        {"id": 231925}, #OS_VMWARE_SERVER_VIRTUALIZATION_6_7_UPDATE_2
        {"id": 876}, # DISK_CONTROLLER_NONRAID
        {"id": 212893}, #HARD_DRIVE_2_00_TB_SATA_2
        {"id": 212893}, #HARD_DRIVE_2_00_TB_SATA_2
        {"id": 50357}, #BANDWIDTH_500_GB
        {"id": 51977}, #10_GBPS_DUAL_PUBLIC_PRIVATE_NETWORK_UPLINKS_UNBONDED
        {"id": 55}, #MONITORING_HOST_PING
        {"id": 58}, #AUTOMATED_NOTIFICATION
        {"id": 420}, #UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT
        {"id": 418}, #NESSUS_VULNERABILITY_ASSESSMENT_REPORTING
        {"id": 21}, #1_IP_ADDRESS
        {"id": 57}, #NOTIFICATION_EMAIL_AND_TICKET
        {"id": 906}, #REBOOT_KVM_OVER_IP
        {"id": 212673}, #VMWARE_VSAN_NODE
        {"id": 212713} #SRIOV_ENABLED
    ],
    "quantity": 1
}

try:
    virtual_host = apiAuthenticationKey.placeOrder(body_json)
    print(json.dumps(virtual_host, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
```
