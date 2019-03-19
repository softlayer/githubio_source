---
title: "Order Static Subnet"
description: "Order and attach the static subnet to an specific ip address in a Vlan"
date: "2019-03-18"
classes: 
    - "SoftLayer_Container_Product_Order_Network_Subnet"
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Product_Order"
tags:
    - "subnets"
    - "order"
---

Such as in the portal page, it is required to select an ip address to order the new static subnet, and to find the available IDs it is recommended to retrieve the subnets either with `Account::getSubnets` or `Network_Vlan::getSubnets`

```
https://api.softlayer.com/rest/v3/SoftLayer_Network_Vlan/12345/getSubnets
```

Next, select a subnet ID and call to `Network_Subnet::getRoutableEndpointIpAddresses` to retrieve the ID of ip addresses which are available to be selected

```
https://api.softlayer.com/rest/v3/SoftLayer_Network_Subnet/67890/getRoutableEndpointIpAddresses
```

This example uses `verifyOrder` method to check the order for errors, replace it by
`placeOrder` method when you are ready to order.

**NOTE:** The Vlan/Subnet must be in the same location you want to order the new static subnet

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
        return items[0], price_id
    
    # Verify ID or VlanNumber exists and returns the vlan ID
    def _resolve_id(self, vlan_id):
        try:
            vlan = self.client['Network_Vlan'].getObject(id=vlan_id)
        except SoftLayer.SoftLayerAPIError:
            _filter = {"networkVlans":{"vlanNumber":{"operation":vlan_id}}}
            vlan_object = self.client['Account'].getNetworkVlans(filter=_filter)
            
            if vlan_object:
                vlan = vlan_object[0]
            else:
                raise

        return vlan['id']

    def _build_answers(self, question_answers, item_category):
        list_answers = []
        
        list_questions = self.client["SoftLayer_Product_Item_Category"].getQuestions(id=item_category["id"])

        for question in question_answers:
            question_id = [q["id"] for q in list_questions if q["keyName"] == question][0]
            question_answer = {
                "categoryId": item_category["id"],
                "categoryCode": item_category["categoryCode"],
                "questionId": question_id,
                "answer": question_answers[question]
            }
            list_answers.append(question_answer)
        
        return list_answers

    def order_subnet(self, package, location, item_keyname, ip_address_id, question_answers=None):
        try:
            packageId = self._get_package_id(package)
            item, priceId = self._get_item_price(packageId, item_keyname)

            orderData = {
                "complexType": "SoftLayer_Container_Product_Order_Network_Subnet",
                "packageId": packageId,
                "location": location,
                "endPointIpAddressId": ip_address_id,    # Set on which vlan we want to attach the subnet
                "prices": [{"id": priceId}],
                "quantity": 1            
            }

            if question_answers:
                orderData["itemCategoryQuestionAnswers"] = self._build_answers(question_answers,
                                                                               item["itemCategory"])
            # verifyOrder will check your order for errors. Replace this with placeOrder
            # when you're ready to order
            return self.client['Product_Order'].verifyOrder(orderData)            
        except SoftLayer.SoftLayerAPIError as e:
            print("Unable to order: %s - %s" % (e.faultCode, e.faultString))
    
if __name__ == "__main__":
    package = "ADDITIONAL_SERVICES_STATIC_IP_ADDRESSES"
    location = "AMSTERDAM"
    
    # set keyname of subnet you want to order
    subnet_type = "1_STATIC_PUBLIC_IP_ADDRESS"
    
    # ID or VlanNumber of the network vlan    
    ip_address_id = 110133117
    
    network = Network()

    # Questions Answers
    # Note: There aren't question_answers for 64_BLOCK_STATIC_PUBLIC_IPV6_ADDRESSES
    answers = {
        "TOTAL_IPS_IN_30_DAYS": 1,
        "TOTAL_IPS_IN_12_MONTHS": 1,
        "REASON_FOR_IPS": "Any reason",
        "CONTACT_NAME": "Jhon Doe",    # Valid name, ex: Jhon Doe
        "CONTACT_JOB_TITLE": "Network Administrator", # Valid job title, ex: Network Administrator
        "CONTACT_EMAIL": "jhondoe@mail.com",
        "CONTACT_PHONE_NUMBER": "555-5555",
        "CONTACT_VALIDATED": 1 # To confirm that the contact information is valid (0 or 1).
    }
    
    receipt = network.order_subnet(package, location, subnet_type, ip_address_id, question_answers=answers)
    pprint(receipt)
```

The python example above allows to create the following subnets which are in the package `ADDITIONAL_SERVICES_STATIC_IP_ADDRESSES`:

- 1_STATIC_PUBLIC_IP_ADDRESS

- 2_STATIC_PUBLIC_IP_ADDRESSES

- 4_STATIC_PUBLIC_IP_ADDRESSES

- 8_STATIC_PUBLIC_IP_ADDRESSES

- 16_STATIC_PUBLIC_IP_ADDRESSES

- 32_STATIC_PUBLIC_IP_ADDRESSES

- 64_STATIC_PUBLIC_IP_ADDRESSES

- 128_STATIC_PUBLIC_IP_ADDRESSES

- 256_STATIC_PUBLIC_IP_ADDRESSES

- 64_BLOCK_STATIC_PUBLIC_IPV6_ADDRESSES