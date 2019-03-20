---
title: "Order Global IP"
description: "Order a global IPv4 or IPv6 "
date: "2019-03-18"
classes: 
    - "SoftLayer_Container_Product_Order_Network_Subnet"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Product_Order"
tags:
    - "subnets"
    - "order"
---

This example uses `verifyOrder` method to check the order for errors, replace it by
`placeOrder` method when you are ready to order.
```python
import SoftLayer
from pprint import pprint

class Network:
    def __init__(self):
        self.client = SoftLayer.Client()

    def _get_package_id(self, keyname):
        _filter = {"type":{"keyName":{"operation":keyname}}}
    
        package = self.client['Product_Package'].getAllObjects(filter=_filter)
        return package[0]['id']
        
    def _get_item_price(self, package_id, item_keyname):
        _filter = {"items":{"keyName":{"operation":item_keyname}}}
        
        items = self.client['Product_Package'].getItems(filter=_filter, id=package_id)

        price_id = [p["id"] for p in items[0]["prices"]
                   if not p["locationGroupId"]][0]
        return price_id
    
    def order_global_ip(self, package, item_keyname):
        packageId = self._get_package_id(package)
        priceId = self._get_item_price(packageId, item_keyname)
            
        orderData = {
            "complexType": "SoftLayer_Container_Product_Order_Network_Subnet",
            "packageId": packageId,
            "prices": [{"id": priceId}],
            "quantity": 1
        }
        
        try:
            # verifyOrder will check your order for errors. Replace this with placeOrder
            # when you're ready to order
            return self.client['Product_Order'].verifyOrder(orderData)
        except SoftLayer.SoftLayerAPIError as e:
            print("Unable to order: %s - %s" % (e.faultCode, e.faultString))

if __name__ == "__main__":
    package = "ADDITIONAL_SERVICES_GLOBAL_IP_ADDRESSES"    
    # Available values are: GLOBAL_IPV4 and GLOBAL_IPV6
    item = "GLOBAL_IPV4"
        
    network = Network()
    receipt = network.order_global_ip(package, item)
    pprint(receipt)
```
