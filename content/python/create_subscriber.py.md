---
title: "create_subscriber.py"
description: "create_subscriber.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer"
tags:
    - "suscribers"
---


```
"""
Create subscribers

The script creates a subscription to an unplanned incident

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/createSubscriberDeliveryMethods
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

try:
    templates = userClient.createSubscriberDeliveryMethods("UNPLANNED_INCIDENT", deliveryMethodKeyNames, id=customerId)
    print(templates)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to create the subscription faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
