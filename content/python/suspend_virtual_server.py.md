---
title: "Working with suspend virtual server"
description: "A few examples on interacting with suspend virtual server."
date: "2019-04-11"
classes: 
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Location"
tags:
    - "virtualserver"
    - "placeorder"
---

###Create Suspend Virtual Server
####SLCLI

```
slcli order place --verify --billing hourly SUSPEND_CLOUD_SERVER DALLAS12 --preset B1_8X16X100 
BANDWIDTH_0_GB_2 1_GBPS_PRIVATE_NETWORK_UPLINK REBOOT_REMOTE_CONSOLE 1_IP_ADDRESS 
UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT OS_WINDOWS_2012_R2_FULL_STD_64_BIT 
MONITORING_HOST_PING NOTIFICATION_EMAIL_AND_TICKET AUTOMATED_NOTIFICATION 
--complex-type SoftLayer_Container_Product_Order_Virtual_Guest 
--extras "{"virtualGuests": [{"hostname":"test", "domain":"softlayer.com"}]}"
```

####Ordering Manager

To get the items KeyNames available to order your VSI, you can use the service SoftLayer_Product_Package::getItemPrices.

```python
import json

import SoftLayer

# Declare the API client
client = SoftLayer.create_client_from_env()

order_manager = SoftLayer.OrderingManager(client)

package_keyname = 'SUSPEND_CLOUD_SERVER'
location = 'DALLAS12'
item_keynames = ['BANDWIDTH_0_GB_2', '1_GBPS_PRIVATE_NETWORK_UPLINK', 'REBOOT_REMOTE_CONSOLE', '1_IP_ADDRESS',
                 'UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT', 'OS_WINDOWS_2012_R2_FULL_STD_64_BIT',
                 'MONITORING_HOST_PING', 'NOTIFICATION_EMAIL_AND_TICKET', 'AUTOMATED_NOTIFICATION',
                 ]

complex_type = 'SoftLayer_Container_Product_Order_Virtual_Guest'
hourly = True
preset_keyname = 'B1_8X16X100'
extras = {"virtualGuests": [{"hostname": "test", "domain": "softlayer.com"}]}
quantity = 1

try:
    result = order_manager.verify_order(package_keyname, location, item_keynames, complex_type=complex_type,
                                        hourly=hourly, preset_keyname=preset_keyname, extras=extras, quantity=quantity)
                                        
    print(json.dumps(result, sort_keys=False, indent=4, separators=(',', ': ')))
    
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to order a Suspend Cloud Server. " % (e.faultCode, e.faultString))
    
```

####Advanced
To get the items KeyNames available to order your VSI, you can use the service SoftLayer_Product_Package::getItemPrices.
```python
import json

import SoftLayer

# Declare the API client
client = SoftLayer.create_client_from_env()

location = 'DALLAS12'

# Package keyName.
package_keyName = 'SUSPEND_CLOUD_SERVER'

# Preset keyName cpu 8, ram 16 GB, first disk 100 GB.
preset_keyName = 'B1_8X16X100'

# Virtual Server Suspend items KeyNames.
items = ['BANDWIDTH_0_GB_2', '1_GBPS_PRIVATE_NETWORK_UPLINK', 'REBOOT_REMOTE_CONSOLE', '1_IP_ADDRESS',
         'UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT', 'OS_WINDOWS_2012_R2_FULL_STD_64_BIT',
         'MONITORING_HOST_PING', 'NOTIFICATION_EMAIL_AND_TICKET', 'AUTOMATED_NOTIFICATION',
         ]

filter_package = {'keyName': {'operation': package_keyName}}

filter_preset = {'activePresets': {'keyName': {'operation': preset_keyName}}}

filter_location = {'regions': {'keyname': {'operation': location}}}

location_list = client["SoftLayer_Location"].getDatacenters(mask='mask[id,name,regions[keyname]]',
                                                            filter=filter_location)
locationId = location_list[0]['id']

package_list = client["SoftLayer_Product_Package"].getAllObjects(filter=filter_package)
packageId = package_list[0]['id']

preset_list = client["SoftLayer_Product_Package"].getActivePresets(mask='mask[prices[item]]',
                                                                   filter=filter_preset, id=packageId)
presetId = preset_list[0]['id']

item_prices = client["SoftLayer_Product_Package"].getItemPrices(mask='mask[item]', id=packageId)

capacity = 0
for preset in preset_list:
    for price in preset['prices']:
        if "CORE" in price['item']['keyName']:
            capacity = price['item']['capacity']

prices = []
for keyname_item in items:
    for item_price in item_prices:
        if keyname_item == item_price['item']['keyName']:
            if 'capacityRestrictionMinimum' in item_price:
                capacityMinimun = item_price['capacityRestrictionMinimum']
                capacityMaximum = item_price['capacityRestrictionMaximum']
                if capacityMinimun >= capacity and capacityMaximum <= capacity:
                    prices.append(item_price['id'])
            else:
                prices.append(item_price['id'])

print(' '.join(map(str, prices)))

orderData = {
    "complexType": "SoftLayer_Container_Product_Order_Virtual_Guest",
    'virtualGuests': [
        {
            'hostname': 'SuspendVsTest',
            'domain': 'softlayer.test'
        }
    ],
    "useHourlyPricing": True,
    'packageId': packageId,
    'location': locationId,
    'presetId': presetId,
    'prices': [{'id': price_id} for price_id in prices],
    'quantity': 1
}

try:
    # Order a virtual guest Suspend.
    response = client['SoftLayer_Product_Order'].placeOrder(orderData)
    print(json.dumps(response, sort_keys=False, indent=4, separators=(',', ': ')))

except SoftLayer.SoftLayerAPIError as e:
    """ 
        If there was an error returned from the SoftLayer API then bomb out with the 
        error message. 
        """
    print("Unable to order a VSI \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```

###Create an Image Template from a Suspend Virtual Server

```python
import json

import SoftLayer

# Declare the API client
client = SoftLayer.create_client_from_env()

virtualGuestId = 11111

block_devices = client['SoftLayer_Virtual_Guest'].getBlockDevices(mask='mask[id,device,diskImage[id,capacity,units]]',
                                                                  id=virtualGuestId)
print(json.dumps(block_devices, sort_keys=False, indent=4, separators=(',', ': ')))

device_list = []
device_num = len(block_devices)
count = 0
while count < len(block_devices):
    print(
        'You have ' + str(device_num) + ' devices to add to your image template, select the "device" number from above'
                                        ' e.g. if "device":"0", enter 0, Or to exit please enter -1')
    devide_data = input()
    if devide_data == "-1":
        break
    else:
        device_list.append(devide_data)
    count = count + 1
    device_num = device_num - 1

block_device_list = []
for data in device_list:
    for device in block_devices:
        if data == device['device']:
            deviceId = device['id']
            block_device_list.append(deviceId)

groupName = "test suspend vs"

blockDevices = [{'id': device_id} for device_id in block_device_list]

note = "test"

try:
    response = client['SoftLayer_Virtual_Guest'].createArchiveTransaction(groupName, blockDevices, note,
                                                                          id=virtualGuestId)
    print(json.dumps(response, sort_keys=False, indent=4, separators=(',', ': ')))

except SoftLayer.SoftLayerAPIError as e:
    """ 
        If there was an error returned from the SoftLayer API then bomb out with the 
        error message. 
        """
    print("Unable to create a image template \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```

###Create a new Suspend Virtual Server from an Image Template

```python
import json

import SoftLayer

# Declare the API client
client = SoftLayer.create_client_from_env()

# Image template id.
imageTemplateId = 11111

location = 'DALLAS12'

# Package keyName.
package_keyName = 'SUSPEND_CLOUD_SERVER'

# Preset keyName cpu 8, ram 16 GB, first disk 100 GB.
preset_keyName = 'B1_8X16X100'

# items KeyNames to be upgraded.
items = ['BANDWIDTH_0_GB_2', '1_GBPS_PRIVATE_NETWORK_UPLINK', 'REBOOT_REMOTE_CONSOLE', '1_IP_ADDRESS',
         'UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT', 'OS_WINDOWS_2012_R2_FULL_STD_64_BIT',
         'MONITORING_HOST_PING', 'NOTIFICATION_EMAIL_AND_TICKET', 'AUTOMATED_NOTIFICATION',
         ]

filter_package = {'keyName': {'operation': package_keyName}}

filter_preset = {'activePresets': {'keyName': {'operation': preset_keyName}}}

filter_location = {'regions': {'keyname': {'operation': location}}}

location_list = client["SoftLayer_Location"].getDatacenters(mask='mask[id,name,regions[keyname]]',
                                                            filter=filter_location)
locationId = location_list[0]['id']
print(locationId)

package_list = client["SoftLayer_Product_Package"].getAllObjects(filter=filter_package)
packageId = package_list[0]['id']
print(packageId)

preset_list = client["SoftLayer_Product_Package"].getActivePresets(mask='mask[prices[item]]',
                                                                   filter=filter_preset, id=packageId)
presetId = preset_list[0]['id']
print(presetId)

item_prices = client["SoftLayer_Product_Package"].getItemPrices(mask='mask[item]', id=packageId)

capacity = 0
for preset in preset_list:
    for price in preset['prices']:
        if "CORE" in price['item']['keyName']:
            capacity = price['item']['capacity']

prices = []
for keyname_item in items:
    for item_price in item_prices:
        if keyname_item == item_price['item']['keyName']:
            if 'capacityRestrictionMinimum' in item_price:
                capacityMinimun = item_price['capacityRestrictionMinimum']
                capacityMaximum = item_price['capacityRestrictionMaximum']
                if capacityMinimun >= capacity and capacityMaximum <= capacity:
                    prices.append(item_price['id'])
            else:
                prices.append(item_price['id'])

print(' '.join(map(str, prices)))

"""
Build a skeleton SoftLayer_Container_Product_Order_Virtual_Guest_Upgrade object
containing the upgrade you wish to place.
"""
orderData = {
    "complexType": "SoftLayer_Container_Product_Order_Virtual_Guest",
    'hardware': [
        {
            'hostname': 'foVsFromImage',
            'domain': 'softlayer.test'
        }
    ],
    "imageTemplateId": imageTemplateId,
    "useHourlyPricing": True,
    'packageId': packageId,
    'location': locationId,
    'presetId': presetId,
    'prices': [{'id': price_id} for price_id in prices],
    'quantity': 1
}

try:
    # Order a virtual guest Suspend.
    response = client['SoftLayer_Product_Order'].placeOrder(orderData)
    print(json.dumps(response, sort_keys=False, indent=4, separators=(',', ': ')))

except SoftLayer.SoftLayerAPIError as e:
    """ 
        If there was an error returned from the SoftLayer API then bomb out with the 
        error message. 
        """
    print("Unable to order a VSI \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```

###Check if a VM is Suspended billing
```python
import SoftLayer

# Declare the API client
client = SoftLayer.create_client_from_env()

virtualGuestId = 11111

package_keyName = "SUSPEND_CLOUD_SERVER"

object_mask = 'mask[blockDeviceTemplateGroup,billingItem[package]]'

try:
    response = client['SoftLayer_Virtual_Guest'].getObject(mask=object_mask, id=virtualGuestId)

    if response['billingItem']['package']['keyName'] == package_keyName:
        print("The virtual server is a " + str(package_keyName))
    else:
        print("The virtual server is not a " + str(package_keyName))

except SoftLayer.SoftLayerAPIError as e:
    """ 
        If there was an error returned from the SoftLayer API then bomb out with the 
        error message. 
        """
    print("Unable to get the virtual server information \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```

###Check status of VM (suspended or not)

```python
import SoftLayer

# Declare the API client
client = SoftLayer.create_client_from_env()

virtualGuestId = 11111

try:
    # Order a virtual guest Suspended.
    response = client['SoftLayer_Virtual_Guest'].getPowerState(id=virtualGuestId)

    if response['keyName'] == "HALTED":
        print("The suspend virtual server is SUSPENDED")
    else:
        print("The suspend virtual server is not SUSPENDED")

except SoftLayer.SoftLayerAPIError as e:
    """ 
        If there was an error returned from the SoftLayer API then bomb out with the 
        error message. 
        """
    print("Unable to get the virtual server power state information \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```

###Get cost related to a Suspended VM
```python
import SoftLayer
from prettytable import PrettyTable

# Declare the API client
client = SoftLayer.create_client_from_env()

virtualGuestId = 11111

object_mask = 'mask[hoursUsed,hourlyRecurringFee,currentHourlyCharge,invoiceItems[recurringFee,hourlyRecurringFee,' \
              'createDate]]'

try:
    billing_response = client['SoftLayer_Virtual_Guest'].getBillingItem(mask=object_mask, id=virtualGuestId)

    state_response = client['SoftLayer_Virtual_Guest'].getPowerState(id=virtualGuestId)
    
    # Get the cost related to a suspended virtual server.
    # Virtual Server is suspended, when it is powerOff. 
    if state_response['keyName'] == "HALTED":
        print("The virtual server is suspended in this case, the usage billing stops here, until the vs is "
              "turned on again. See the billing information below")
    else:
        print("The virtual server is not SUSPENDED in this case, will continue with the billing of use. "
              "See the billing information below until now")
        
    table = PrettyTable(['hoursUsed', 'hourlyRecurringFee', 'currentHourlyCharge'])
    table.add_row([
        billing_response['hoursUsed'],
        billing_response['hourlyRecurringFee'],
        billing_response['currentHourlyCharge']
    ])
    print(table)

except SoftLayer.SoftLayerAPIError as e:
    """ 
        If there was an error returned from the SoftLayer API then bomb out with the 
        error message. 
        """
    print("Unable to get the virtual server billing item invoice information \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```
