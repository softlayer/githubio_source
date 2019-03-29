---
title: "Order a Netscaler"
description: "Example of how to order a Citrix NetScaler."
date: "2019-03-28"
classes:
    - "SoftLayer_Product_Order"
tags:
    - "netscaler"
    - "vpx"
    - "order"
---
```py
import SoftLayer
from pprint import pprint

class Network:
    def __init__(self):
        client = SoftLayer.Client()
        self.package_service = client['Product_Package']
        self.order_service = client['Product_Order']

    def print_available_locations(self, package_id):
        pass
        regions = self.package_service.getRegions(id=package_id)

        for region in regions:
            print("\n%s | %s | %s" % 
                (region["location"]["locationId"], 
                 region["keyname"], 
                 region["description"]))
    
    def print_available_items(self, package_id):
        _mask = "mask[id, description, keyName]"
        items = self.package_service.getItems(mask=_mask, id=package_id)

        for item in items:
            print("\n%s | %s | %s" % (item["id"], item["keyName"], item["description"]))
    
    def get_package_id(self, keyname):
        _filter = {"type":{"keyName":{"operation":keyname}}}
    
        package = self.package_service.getAllObjects(filter=_filter)
        return package[0]['id']

    def _get_item_prices(self, package_id, keynames):
        items = self.package_service.getItems(id=package_id)

        prices = []        
        for item_keyname in keynames:
            try:
                item = [i for i in items if i["keyName"] == item_keyname][0]
            except IndexError:
                print("ERROR: Item {} doesn't exist".format(item_keyname))
                exit(0)
            
            price_id = [p["id"] for p in item["prices"] if not p["locationGroupId"]][0]

            prices.append(price_id)
        
        return prices

    def order_netscaler(self, package_id, location, items,
                        fvlan=None, bvlan=None, verify=False):

        prices = self._get_item_prices(package_id, items)

        orderData = {
            "complexType": "SoftLayer_Container_Product_Order_Network_Application_Delivery_Controller",
            "packageId": package_id,
            "location": location,
            "prices": [{'id': price_id} for price_id in prices],
            "quantity": 1
        }

        hardware = {}
        if fvlan:
            hardware["primaryNetworkComponent"] = {"networkVlan":{"id": fvlan}}
        
        if bvlan:
            hardware["primaryBackendNetworkComponent"] = {"networkVlan":{"id": bvlan}}
        
        if hardware:
            orderData["hardware"] = [hardware]
        
        try:
            if verify:
                return self.order_service.verifyOrder(orderData)
            else:
                return self.order_service.placeOrder(orderData)                
        except SoftLayer.SoftLayerAPIError as e:
            print("Unable to order: %s - %s" % (e.faultCode, e.faultString))
        

if __name__ == "__main__":
    package = "ADDITIONAL_SERVICES_APPLICATION_DELIVERY_APPLIANCE"
   
    network = Network()
    package_id = network.get_package_id(package)
    
    # Uncomment the following to see the list of locations and items you can select
    # network.print_available_locations(package_id)
    # network.print_available_items(package_id)

    location = "AMSTERDAM03"
    
    item_keynames = [
        "CITRIX_NETSCALER_VPX_10_1_10MBPS_STANDARD",    # Netscaler
        "4_STATIC_PUBLIC_IP_ADDRESSES"                  # ip address
    ]

    # The vlans you want assign to the netscaler (optional)
    public_vlan = 12345
    private_vlan = 67890

    # Remove verify=True or set it False when you ready to order
    receipt = network.order_netscaler(package_id, location, item_keynames, 
                                      fvlan=public_vlan, bvlan=private_vlan, verify=True)
    pprint(receipt)

```
