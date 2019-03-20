---
title: "Order Portable Subnet"
description: "Add portable private/public subnet to a Vlan"
date: "2019-03-15"
classes: 
    - "SoftLayer_Container_Product_Order_Network_Subnet"
    - "SoftLayer_Product_Order"
tags:
    - "subnets"
    - "vlans"
    - "vlan"
    - "order"
---
This example uses the `verifyOrder` method to check the order for errors, replace it by
`placeOrder` method when you are ready to order.

**NOTE:** The selected Vlan must be in the same location you want to order the new portable subnet

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

    def order_subnet(self, package, location, item_keyname, vlan_number, question_answers=None):
        try:
            packageId = self._get_package_id(package)
            item, priceId = self._get_item_price(packageId, item_keyname)            
            vlan_id = self._resolve_id(vlan_number)       

            orderData = {
                "complexType": "SoftLayer_Container_Product_Order_Network_Subnet",
                "packageId": packageId,
                "location": location,
                "endPointVlanId": vlan_id,    # Set on which vlan we want to attach the subnet
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
    package = "ADDITIONAL_SERVICES_PORTABLE_IP_ADDRESSES"
    location = "AMSTERDAM"
    
    # set 4_PORTABLE_PRIVATE_IP_ADDRESSES if you want a private subnet
    subnet_type = "4_PORTABLE_PUBLIC_IP_ADDRESSES"
    
    # ID or VlanNumber of the network vlan
    # Set a PRIVATE Vlan if you want to order a private subnet
    vlan_id = 994
    
    network = Network()

    # Questions Answers
    # Note: There aren't question_answers for 64_BLOCK_PORTABLE_PUBLIC_IPV6_ADDRESSES
    answers = {
        "TOTAL_IPS_IN_30_DAYS": 1,
        "TOTAL_IPS_IN_12_MONTHS": 4,
        "REASON_FOR_IPS": "Any reason",
        "CONTACT_NAME": "Jhon Doe",    # Valid name, ex: Jhon Doe
        "CONTACT_JOB_TITLE": "Network Administrator", # Valid job title, ex: Network Administrator
        "CONTACT_EMAIL": "jhondoe@mail.com",
        "CONTACT_PHONE_NUMBER": "555-5555",
        "CONTACT_VALIDATED": 1 # To confirm that the contact information is valid (0 or 1).
    }
    
    receipt = network.order_subnet(package, location, subnet_type, vlan_id, question_answers=answers)
    pprint(receipt)
```

The python example above allows to create the following subnets which are in the package `ADDITIONAL_SERVICES_PORTABLE_IP_ADDRESSES`:


|              Public Subnets             |          Private Subnets          |
|-----------------------------------------|-----------------------------------|
| 4_PORTABLE_PUBLIC_IP_ADDRESSES          | 4_PORTABLE_PRIVATE_IP_ADDRESSES   |
| 8_PORTABLE_PUBLIC_IP_ADDRESSES          | 8_PORTABLE_PRIVATE_IP_ADDRESSES   |
| 16_PORTABLE_PUBLIC_IP_ADDRESSES         | 16_PORTABLE_PRIVATE_IP_ADDRESSES  |
| 32_PORTABLE_PUBLIC_IP_ADDRESSES         | 32_PORTABLE_PRIVATE_IP_ADDRESSES  |
| 64_PORTABLE_PUBLIC_IP_ADDRESSES         | 64_PORTABLE_PRIVATE_IP_ADDRESSES  |
| 128_PORTABLE_PUBLIC_IP_ADDRESSES        | 128_PORTABLE_PRIVATE_IP_ADDRESSES |
| 256_PORTABLE_PUBLIC_IP_ADDRESSES        | 256_PORTABLE_PRIVATE_IP_ADDRESSES |
| 64_BLOCK_PORTABLE_PUBLIC_IPV6_ADDRESSES |                                   |