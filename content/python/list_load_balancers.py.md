---
title: "list_load_balancers.py"
description: "list_load_balancers.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress"
tags:
    - "loadbalancers"
---


```
"""
List the load balancers in the account.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getAdcLoadBalancers
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
accountService = client['SoftLayer_Account']

objectMask = "mask[id, connectionLimit, connectionLimitUnits, dedicatedFlag, notes, highAvailabilityFlag, ipAddress, securityCertificateId, sslActiveFlag, sslEnabledFlag, loadBalancerHardware[hostname, fullyQualifiedDomainName, datacenterName], dedicatedBillingItem[id, description, cancellationDate], billingItem[id, upgradeItem, description, cancellationDate], applicationDeliveryControllers[id]]"

try:
    loadBalancers = accountService.getAdcLoadBalancers(mask=objectMask)
    data = []
    for loadBalancer in loadBalancers:
        record = {}
        record['id'] = loadBalancer['id']
        record['vipAddress'] = loadBalancer['ipAddress']['ipAddress']
        record['device'] = loadBalancer['loadBalancerHardware'][0]['hostname']
        record['location'] = loadBalancer['loadBalancerHardware'][0]['datacenterName']
        if 'notes' in loadBalancer:
            record['notes'] = loadBalancer['notes']
        record['notes'] = ''
        if loadBalancer['sslEnabledFlag']:
            if loadBalancer['sslActiveFlag']:
                record['ssl'] = "Enabled"
            else:
                record['ssl'] = "Disabled"
        else:
            record['ssl'] = "Not Supported"
        record['connectionsSecond'] = loadBalancer['connectionLimit']
        data.append(record)
    print(json.dumps(data, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the load balancers. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
