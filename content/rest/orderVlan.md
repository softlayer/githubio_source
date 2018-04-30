---
title: "How to order Vlans"
description: "Shows how to properly place an order for a VLAN."
date: "2018-03-02"
classes: 
    - "SoftLayer_Network_Vlan"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Product_Item_Category"
tags:
  - "vlans"
  - "Product"
  - "placeOrder"
---

There are a few steps in preparing to order a VLAN.

## Find the DC name
Lets start by finding the datacenter we want to order in.

```
curl -u $SL_USER:$SL_APIKEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Package/571/getRegions.json?objectMask=mask\[description,keyname\]' | python -m json.tool
```

Keep track of the KeyName of the location you want to order from.

```
[{"description": "HOU02 - Houston", "keyname": "HOUSTON02" }]
```
## Find the correct router (optional)
If you want the new VLAN to be behind a specific router, you need to find the ID of that router.

To get a list of all the routers your account currently has VLANs on, you can use 
```
curl -u $SL_USER:$SL_APIKEY "https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getRouters?objectMask=mask\[hostname,id\]" | python -m json.tool
```

```
[{ "hostname": "bcr02a.hou02", "id": 112661 },]
```

If you have a Vyatta or other device you want this VLAN to be accessible to, you can find the Vyattas router and just use that.

This will list all Gateway devices and their routers
```
curl -u $SL_USER:$SL_APIKEY "https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getNetworkGateways?objectMask=mask\[members\[hardware\[backendRouters\[hostname,id\],frontendRouters\[hostname,id\]\]\]\]" | python -m json.tool
```

This will list a specific gateway device and its routers
```
curl -u $SL_USER:$SL_APIKEY "https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Gateway/172123/getObject?objectMask=mask\[members\[hardware\[backendRouters\[hostname,id\],frontendRouters\[hostname,id\]\]\]\]" | python -m json.tool
```

Which will output something like this. For Public VLANs, you will want the ID of the frontend router, for Private, the backend router. If there are 2 routers, use the id from the router labeled A
```json
{
    "id": 172123,
    "name": "houstonvpndemo",
    "members": [
        {
            "hardwareId": 149607,
            "id": 201323,
            "networkGatewayId": 172123,
            "hardware": {
                "fullyQualifiedDomainName": "houstonvpndemo.example.com",
                "id": 149607,
                "backendRouters": [
                    {
                        "hostname": "bcr02a.hou02",
                        "id": 112661
                    },
                    {
                        "hostname": "bcr02b.hou02",
                        "id": 112660
                    }
                ],
                "frontendRouters": [
                    {
                        "hostname": "fcr02a.hou02",
                        "id": 112561
                    },
                    {
                        "hostname": "fcr02b.hou02",
                        "id": 112560
                    }
                ]
            }
        }
        ]
    }
```

For this example, we are going to use "fcr02a.hou02", or id=112561


## Find the price IDs
This is a several step process. The [SLCLI](https://softlayer-python.readthedocs.io/en/latest/cli/ordering.html) has a few helper functions for this. For this example though I will walk you through each REST call needed

#### Find the package

This will get all packages that are NOT bluemix services.
```
curl -u $SL_USER:$SL_APIKEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Package/getAllObjects.json?objectMask=mask\[id,name,keyName,isActive,type\]&objectFilter=\{"type":\{"keyName":\{"operation":"!=BLUEMIX_SERVICE"\}\}\}'
```

One of the results is going to be NETWORK_VLAN, which is what we want.
```json
{
    "id": 571,
    "isActive": 1,
    "keyName": "NETWORK_VLAN",
    "name": "Network VLAN",
    "type": {
        "id": 495,
        "keyName": "ADDITIONAL_SERVICES_NETWORK_VLAN",
        "name": "Network VLAN"
    }
}
```


Since packages ids can change, it is a good idea to look these up in the future based on their keyName. *This object filter starts at keyName, the one above starts at type*

```
curl -u $SL_USER:$SL_APIKEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Package/getAllObjects.json?objectMask=mask\[id,name,keyName,isActive,type\]&objectFilter=\{"keyName":\{"operation":"NETWORK_VLAN"\}\}'
```

#### Find the price ids

From the above example, we know we need to get the items from package 571
```
curl -u $SL_USER:$SL_APIKEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Package/571/getItems.json?objectMask=mask\[id,keyName,itemCategory,prices\[id,locationGroupId\]\]' | python -m json.tool
```

The result should be similar to this. If a price has multiple ids, use the one iwth a locationGroupId = null
```json
[
    {
        "id":1072, 
        "keyName":"PRIVATE_NETWORK_VLAN"
        "itemCategory": {
            "categoryCode": "network_vlan",
            "id": 113,
            "name": "Network Vlan",
            "quantityLimit": 0,
            "sortOrder": null
        }
        "prices": [
            {
                "id": 2019,
                "locationGroupId": null
            }
        ]
    },
    {
        "id":583, 
        "keyName":"8_STATIC_PUBLIC_IP_ADDRESSES"
        "itemCategory": {
            "categoryCode": "static_sec_ip_addresses",
            "id": 53,
            "name": "Public Secondary Static IP Addresses",
            "quantityLimit": 0,
            "sortOrder": 35
        }
        "prices": [
            {
                "id": 36696,
                "locationGroupId": null
            }
        ]
    }
]
```

#### Answer the IP useage questions

[getQuestions](https://softlayer.github.io/reference/services/SoftLayer_Product_Item_Category/getQuestions/)

When ordering a new subnet of IP space, a few questions need to be answered for our records.  

ID 53 is from the above item category id. 
```
curl -u $SL_USER:$SL_APIKEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Item_Category/53/getQuestions.json' | python -m json.tool
```

That will return a long list of questions you need to answer, which we will have to add when we make our order.



## Placeing the order
Now that we have all the required information, we can build an order object.



#### order.json
```json
{
  "parameters": [
    {
      "location": "HOUSTON02",
      "routerId": 112661,
      "packageId": 571,
      "prices": [
        {
          "id": 2019 
        },
        {
          "id": 36696 
        }
      ],
      "quantity": 1,
      "name": "myNewVlan",
      "complexType": "SoftLayer_Container_Product_Order_Network_Vlan",
      "itemCategoryQuestionAnswers": [
        {
          "categoryId": 53,
          "categoryCode": "static_sec_ip_addresses",
          "questionId": 14,
          "answer": 4 
        },
        {
          "categoryId": 53,
          "categoryCode": "static_sec_ip_addresses",
          "questionId": 15,
          "answer": 8 
        },
        {
          "categoryId": 53,
          "categoryCode": "static_sec_ip_addresses",
          "questionId": 16,
          "answer": "For more machines"
        },
        {
          "categoryId": 53,
          "categoryCode": "static_sec_ip_addresses",
          "questionId": 9,
          "answer": "Chris"
        },
        {
          "categoryId": 53,
          "categoryCode": "static_sec_ip_addresses",
          "questionId": 10,
          "answer": "Developer"
        },
        {
          "categoryId": 53,
          "categoryCode": "static_sec_ip_addresses",
          "questionId": 11,
          "answer": "chris@company.com"
        },
        {
          "categoryId": 53,
          "categoryCode": "static_sec_ip_addresses",
          "questionId": 12,
          "answer": "1234567890"  
        },
        {
          "categoryId": 53,
          "categoryCode": "static_sec_ip_addresses",
          "questionId": 13,
          "answer": true  
        }
      ]
    }
  ]
}
```

After you create your order container file, then we should use [verifyOrder](https://softlayer.github.io/reference/services/SoftLayer_Product_Order/verifyOrder/) to make sure our data is ok.

```
curl -u $SL_USER:$SL_APIKEY  --data @order.json  'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Order/verifyOrder'
```

If you get back a json object, then it should be ok to order.

```
curl -u $SL_USER:$SL_APIKEY -X POST  --data @order.json  'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Order/placeOrder'
```

If successful, you should get a large json object as a reciept when done. This will have your orderId on it, so you can look it up if needed.

My order id was 23530337, so I will use the [SoftLayer_Billing_Order](https://softlayer.github.io/reference/services/SoftLayer_Billing_Order/getObject/) setvice to view it.
```
curl -u $SL_USER:$SL_APIKEY  'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Order/23530337/getObject'
```
