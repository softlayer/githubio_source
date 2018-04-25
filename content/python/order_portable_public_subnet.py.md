---
title: "order_portable_public_subnet.py"
description: "order_portable_public_subnet.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order_Network_Subnet"
    - "SoftLayer_Product_Order"
tags:
    - "subnets"
---


```
"""
Orders a new portable public subnet

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder/
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder/

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer
# For nice debug output:
from pprint import pprint as pp

API_USERNAME = 'set me'
API_KEY = 'set me'

# Order Template with all new item configurations

orderTemplate = {
    'location': 224092,    # Singapore 1
    'packageId': 0,
    'endPointVlanId': 527900,
    'prices': [
        {
            'id': 13980
        }
    ],
    'quantity': 1,
    'itemCategoryQuestionAnswers': [
        {
            'categoryId': 313,
            'categoryCode': 'sov_sec_ip_addresses_pub',
            'questionId': 14,
            'answer': 1    # TOTAL_IPS_IN_30_DAYS
        },
        {
            'categoryId': 313,
            'categoryCode': 'sov_sec_ip_addresses_pub',
            'questionId': 15,
            'answer': 3    # TOTAL_IPS_IN_12_MONTHS
        },
        {
            'categoryId': 313,
            'categoryCode': 'sov_sec_ip_addresses_pub',
            'questionId': 16,
            'answer': 'Test description of your need for additional IPs'     # REASON_FOR_IPS
        },
        {
            'categoryId': 313,
            'categoryCode': 'sov_sec_ip_addresses_pub',
            'questionId': 9,
            'answer': 'ContactNameTest'    # CONTACT_NAME
        },
        {
            'categoryId': 313,
            'categoryCode': 'sov_sec_ip_addresses_pub',
            'questionId': 10,
            'answer': 'ContactJobTitleTest'    # CONTACT_JOB_TITLE
        },
        {
            'categoryId': 313,
            'categoryCode': 'sov_sec_ip_addresses_pub',
            'questionId': 11,
            'answer': 'contact.email@myemail.com'    # CONTACT_EMAIL
        },
        {
            'categoryId': 313,
            'categoryCode': 'sov_sec_ip_addresses_pub',
            'questionId': 12,
            'answer': '72878781'    # CONTACT_PHONE_NUMBER
        },
        {
            'categoryId': 313,
            'categoryCode': 'sov_sec_ip_addresses_pub',
            'questionId': 13,
            'answer': True    # CONTACT_VALIDATED
        }
    ],
    'complexType': 'SoftLayer_Container_Product_Order_Network_Subnet'
}

# Creates a new connection to the API service.
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
