---
title: "Order an external authentication"
description: "It allows to order external authentication like 'Symantec Identity Protection' or 'Phone-based authentication' "
date: "2018-09-26"
classes: 
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_User_Customer_External_Binding"
tags:
    - "order"
    - "user"
---

```python
import SoftLayer
import json

class example():
    def __init__(self):
        self.client = SoftLayer.Client()

    # Generate the order template used to place the order
    def _generateOrder(self, userId, keyName, package, credential=None):
        # Retrieve the package object in order to know its ID
        pkg_filter = {"keyName":{"operation": package}}
        package_list = self.client['Product_Package'].getAllObjects(filter=pkg_filter)
        package_id = package_list[0]['id']

        # Retrive the available price of external auth item
        itm_filter = {"itemPrices":{"item":{"keyName":{"operation":keyName}}}}
        prices = self.client['Product_Package'].getItemPrices(filter=itm_filter, id=package_id)

        # Build skeleton of order template
        orderTemplate = {
            'complexType': 'SoftLayer_Container_Product_Order_User_Customer_External_Binding',
            'packageId': package_id,
            'prices':[{'id': prices[0]['id']}],
            'userId': userId,
            'externalId': credentialId
        }
        
        return orderTemplate

    def orderExternalAuth(self, userId, keyName, credential=None):
        # package used to order an External Auth.
        package_name = 'AUTHENTICATION_SERVICES'
        
        order_template = self._generateOrder(userId, keyName, package_name, 
                                             credential=credential)

        order_service = self.client['Product_Order']
        try:
            # verifyOrder() will check your order for errors. Replace this with a call
            # to placeOrder() when you're ready to order 
            receipt = order_service.verifyOrder(order_template)

            print(json.dumps(receipt, sort_keys=True, indent=2, separators=(',', ': ')))
        except (SoftLayer.SoftLayerAPIError) as e:            
            print("Unable to order external auth: %s, %s" % (e.faultCode, e.faultString))

if __name__ == "__main__":
    # The user id on which the external auth will be attached. 
    # Users are able to order an external auth by themselves, but if you want to order 
    # for other users  then use the credentials of the Master User
    user_id = 66252

    # Key name of external auth you want to order, select between:
    # SYMANTEC_IDENTITY_PROTECTION or PHONEBASED_AUTHENTICATION
    keyName = 'SYMANTEC_IDENTITY_PROTECTION'
    
    # Items like SYMANTEC_IDENTITY_PROTECTION requires a credential id
    # It isn't required for PHONEBASED_AUTHENTICATION
    credentialId = 'ASD5675d6DDD7'

    main = example()
    main.orderExternalAuth(user_id, keyName, credential=credentialId)

```