---
title: "update_subscriber.py"
description: "update_subscriber.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer"
tags:
    - "suscribers"
---


```
"""
Update subscribers

The script updates a subscription to an unplanned incident

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/updateSubscriberDeliveryMethod
http://sldn.softlayer.com/reference/datatypes/SoftLayer_User_Customer

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

USERNAME = 'set me'
API_KEY = 'set me'

# The customer ID you wish add the subscription
customerId = 205830

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
userClient = client['SoftLayer_User_Customer']


deliveryMethodKeyNames = [
    "EMAIL"
]

# The status 0 = inactive; 1= active
status = 0

try:
    templates = userClient.updateSubscriberDeliveryMethod("UNPLANNED_INCIDENT", deliveryMethodKeyNames, status, id=customerId)
    print(templates)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to update the subscription faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
