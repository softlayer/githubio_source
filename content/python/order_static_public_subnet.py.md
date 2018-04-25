---
title: "order_static_public_subnet.py"
description: "order_static_public_subnet.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order_Network_Subnet"
    - "SoftLayer_Product_Order"
tags:
    - "subnets"
---


```
"""
Orders a new static public subnet

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder/
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder/

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

# Order a new SoftLayer IP subnet
import SoftLayer
# For nice debug output:
from pprint import pprint as pp

API_USERNAME = 'set me'
API_KEY = 'set me'

# Order Template with all configurations of the new item
orderTemplate = {
    'location': 154820,     # dal06
    'packageId': 0,
    'endPointIpAddressId': 24036066,
    'prices': [
        {
            'id': 13983
        }
    ],
    'quantity': 1,
    'itemCategoryQuestionAnswers': [
        {
            'categoryId': 53,
            'categoryCode': 'static_sec_ip_addresses',
            'questionId': 14,
            'answer': 1     # static_sec_ip_addresses
        },
        {
            'categoryId': 53,
            'categoryCode': 'static_sec_ip_addresses',
            'questionId': 15,
            'answer': 1    # TOTAL_IPS_IN_12_MONTHS
        },
        {
            'categoryId': 53,
            'categoryCode': 'static_sec_ip_addresses',
            'questionId': 16,
            'answer': 'Set the description of your need for additional IPs'     # TOTAL_IPS_IN_12_MONTHS
        },
        {
            'categoryId': 53,
            'categoryCode': 'static_sec_ip_addresses',
            'questionId': 9,
            'answer': 'ContactNameTest'     # TOTAL_IPS_IN_12_MONTHS
        },
        {
            'categoryId': 53,
            'categoryCode': 'static_sec_ip_addresses',
            'questionId': 10,
            'answer': 'ContactJobTitle'    # CONTACT_JOB_TITLE
        },
        {
            'categoryId': 53,
            'categoryCode': 'static_sec_ip_addresses',
            'questionId': 11,
            'answer': 'contact.email@email.com'    # CONTACT_EMAIL
        },
        {
           'categoryId': 53,
           'categoryCode': 'static_sec_ip_addresses',
           'questionId': 12,
           'answer': '72878781'    # CONTACT_PHONE_NUMBER
        },
        {
           'categoryId': 53,
           'categoryCode': 'static_sec_ip_addresses',
           'questionId': 13,
           'answer': True    # CONTACT_PHONE_NUMBER
        }
    ],
    'complexType': 'SoftLayer_Container_Product_Order_Network_Subnet'
    }

client = SoftLayer.Client(
    username=API_USERNAME,
    api_key=API_KEY
)

try:
    result = client['SoftLayer_Product_Order'].verifyOrder(orderTemplate)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    pp('Failed ... Unable to order the new item faultCode=%s, faultString=%s'
        % (e.faultCode, e.faultString))

```
