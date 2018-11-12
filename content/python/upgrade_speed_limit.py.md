---
title: "Upgrade Local Load Balancer"
description: "It upgrades the connection speed limit"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress"
tags:
    - "loadbalancers"
---


```python
import SoftLayer
import json

class example():
    def __init__(self):
        self.client = SoftLayer.Client()

    # Retrieves the next recurring fee and description
    def _getNextPrice(self, lbID, service):
        objMask = 'mask[id,billingItem[id,description,upgradeItem]]'

        try:
            lbalancer = service.getObject(mask=objMask, id=lbID)
            
            upgrade_item = lbalancer['billingItem']['upgradeItem']
            recurringFee = [p['recurringFee'] for p in upgrade_item['prices']
                            if not p['locationGroupId']][0]
            
            price_dict = {
                "description": upgrade_item['description'],
                "recurringFee": recurringFee,
                "capacity" : upgrade_item['capacity'] + " " + upgrade_item['units']
            }
            return price_dict

        except (SoftLayer.SoftLayerAPIError) as e:
            print("Unable to retrieve next price: %s, %s" % (e.faultCode, e.faultString))
    
    # private method which helps to retrieve an input 
    def _wantUpgrade(self):
        answer = None
        while answer not in ['y', 'n']:
            answer = raw_input("\nAre you sure you want to upgrade? (y/n):")
            answer = answer.lower()
                
            if answer == 'y':                    
                return True
            elif answer == 'n':
                return False
            else:
                print('Please answer with y or n')

    # If user send 'y' then upgrade the LB
    def upgradeItem(self, lbID):
        lbalancer_service = self.client['Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress']

        try:
            next_price = self._getNextPrice(lbID, lbalancer_service)
            print("\nThis will upgrade to %s and change the recurring fee to $%s" % 
                  (next_price['description'], next_price['recurringFee']))
            
            if self._wantUpgrade():
                if lbalancer_service.upgradeConnectionLimit(id=lbID):
                    print('The Load Balancer %s was upgraded to %s' % (lbID, next_price['capacity']))

        except (SoftLayer.SoftLayerAPIError) as e:            
            print("Unable to upgrade: %s, %s" % (e.faultCode, e.faultString))

if __name__ == "__main__":
    # ID of LBaaS
    load_balancer_id = 33184
    
    main = example()
    main.upgradeItem(load_balancer_id)
```
*Example:*

```
This will upgrade to Load Balancer 1,000 VIP Connections and change the recurring fee to $199.99

Are you sure you want to upgrade? (y/n):y
The Load Balancer 33184 was upgraded to 1000 Connections/Second

```