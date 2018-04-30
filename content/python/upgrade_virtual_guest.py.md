---
title: "upgrade_virtual_guest.py"
description: "upgrade_virtual_guest.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_Virtual_Guest_Upgrade"
tags:
    - "virtualserver"
---


```
"""
Upgrade a VSI.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder/
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder/


License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer
# For nice debug output:
from pprint import pprint as pp

# Your SoftLayer API username and key.
API_USERNAME = 'set me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set me'

virtualGuestId = 35747489

orderContainer = {}
orderContainer['complexType'] = 'SoftLayer_Container_Product_Order_Virtual_Guest_Upgrade'
orderContainer['virtualGuests'] = [{'id': virtualGuestId}]
orderContainer['prices'] = [
    # RAM Upgrades, uncomment the desired one
    {'id': 1644}  # 1 GB RAM
    #  {'id': 1645 } # 2 GB RAM
    # {'id': 1646 } # 4 GB RAM
    # {'id': 2238 } # 6 GB RAM
    # {'id': 1647 } # 8 GB RAM
    # {'id': 2243 } # 12 GB RAM
    # {'id': 1927 } # 16 GB RAM
    # {'id': 21275 } # 32 GB RAM
    # {'id': 22422 } # 48 GB RAM
    # {'id': 37042 } # 64 GB RAM

    # CPU Upgrades, uncomment the desired one
    # {'id': 1962 } # Private 1 x 2.0 GHz Core
    # {'id': 1963 } # Private 2 x 2.0 GHz Cores
    # {'id': 1964 } # Private 4 x 2.0 GHz Cores
    # {'id': 1965 } # Private 8 x 2.0 GHz Cores
    # {'id': 2156 } # 1 x 2.0 GHz Internal Core
    # {'id': 1640 } # 1 x 2.0 GHz Core
    # {'id': 1641 } # 2 x 2.0 GHz Cores
    # {'id': 1642 } # 4 x 2.0 GHz Cores
    # {'id': 1643 } # 8 x 2.0 GHz Cores
    # {'id': 2231 } # 12 x 2.0 GHz Cores
    # {'id': 2235 } # 16 x 2.0 GHz Cores
]
orderContainer['properties'] = [{'name': 'MAINTENANCE_WINDOW', 'value': 'now'}]

orderClient = SoftLayer.create_client_from_env(
    username=API_USERNAME,
    api_key=API_KEY
)

"""
verifyOrder() will check your order for errors. Replace this with a call to
placeOrder() when you're ready to order. Both calls return a receipt object
that you can use for your records.

Once your order is placed it'll go through SoftLayer's provisioning process.
When it's done you'll have a new SoftLayer_Virtual_Guest object and CCI ready
to use.
"""
try:
    result = orderClient['Product_Order'].verifyOrder(orderContainer)
    pp(result)

except SoftLayer.SoftLayerAPIError as e:
        pp('Unable to upgrade the VSI faultCode=%s, faultString=%s'
            % (e.faultCode, e.faultString))

```
