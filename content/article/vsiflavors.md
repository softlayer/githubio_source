---
title: "VSI Flavors"
description: "Our public virtual server offering now comes in four distinct virtual server families: balanced, balanced local storage, compute, and memory. With this enhancement, IBM continues its effort to provide you with a first-class public cloud experience by taking the guesswork out of provisioning the right instance flavor for your workload needs."
date: "2018-03-12"
author: "cgallo"
tags:
    - "article"
    - "slcli"
    - "ordering"
    - "order"
    - "vsi"
    - "virtualserver"
---

The introduction of Flavors to VSI ordering significantly changes how VSIs are ordered, and the old style of ordering will eventually become unsupported. This page will hopefully explain what changes need to be made to any scripts that order VSIs.

Support for flavors has been added to the [SLCLI](https://github.com/softlayer/softlayer-python), so make sure you have at least version 5.4.0.


# Getting a Flavor List

[SoftLayer_Virtual_Guest::getCreateObjectOptions](https://softlayer.github.io/reference/services/SoftLayer_Virtual_Guest/getCreateObjectOptions/) is where you can find out the flavor listing, along with all other options you might want to supply to [SoftLayer_Virtual_Guest::createObject](https://softlayer.github.io/reference/services/SoftLayer_Virtual_Guest/createObject)

In the response from getCreateObjectOptions, will be a key "flavors", with an array of different flavors and some information about their configuration.

```
$ curl -g -u ${SLAUTH} "https://api.softlayer.com/rest/v3/SoftLayer_Virtual_Guest/getCreateObjectOptions" | python -m json.tool


{ommitted}
    "flavors": [
        {
            "flavor": {
                "keyName": "B1_1X2X25",
                "name": "B1.1x2x25",
                "configuration": [
                    {
                        "category": {
                            "name": "First Disk"
                        },
                        "price": {
                            "hourlyRecurringFee": "0",
                            "item": {
                                "description": "25 GB (SAN)"
                            }
                        }
                    },
                    {
                        "category": {
                            "name": "RAM"
                        },
                        "price": {
                            "hourlyRecurringFee": ".03",
                            "item": {
                                "description": "2 GB"
                            }
                        }
                    },
                    {
                        "category": {
                            "name": "Computing Instance"
                        },
                        "price": {
                            "hourlyRecurringFee": ".023",
                            "item": {
                                "description": "1 x 2.0 GHz Core"
                            }
                        }
                    }
                ],
                "totalMinimumHourlyFee": "0.053",
                "totalMinimumRecurringFee": "35.17"
            },
            "template": {
                "id": null,
                "supplementalCreateObjectOptions": {
                    "flavorKeyName": "B1_1X2X25"
                }
            }
        },
{ommitted}
```

The same information can be retrieved from the SLCLI as well.
```
slcli vs create-options
```


# Ordering a Flavor


Basically, instead of specifying a CPU, Memory, and Disk specifically, you remove those options and instead add a new "[supplementalCreateObjectOptions](https://softlayer.github.io/reference/datatypes/SoftLayer_Virtual_Guest_SupplementalCreateObjectOptions/)" field that has the flavor. Here is a [REST Example](https://console.bluemix.net/docs/vsi/vsi_provision_api.html#api-rest-public)

And here is how to use the SLCLI for ordering
```
slcli vs create --os=UBUNTU_LATEST_64 \
    --flavor=BL1_2X4X100  \
    --billing=hourly  \
    --domain=softlayer.com  \
    --hostname=sldn-testing  \
    --datacenter=hou02
```

# Getting a flavor of a VSI existent 


[SoftLayer_Virtual_Guest::getObject](https://softlayer.github.io/reference/services/SoftLayer_Virtual_Guest/getObject/)  is where you can find out the flavor preset of the VSI specific, use with a mask to getting the information

In the response from getObject, will be a VSI information, and with information about their flavor [preset](https://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Order_Item/#preset).


``` 
curl -u $SL_USER:$SL_APIKEY -X GET -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress" 'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/11223344/getObject.json?objectMask=mask%5BbillingItem%5BorderItem%5Bpreset%5D%5D%5D'
```

The same information can be retrieved from the SLCLI as well.


```bash
slcli --format=json call-api Virtual_Guest getObject 
          --id=123456 
          --mask=billingItem.orderItem.preset
```


# Getting a order of a VSI existent

[SoftLayer_Virtual_Guest::getObject](https://softlayer.github.io/reference/services/SoftLayer_Virtual_Guest/getObject/) is where you can find out the order details of the VSI specific, use with a mask to getting the information

In the response from getObject, will be a VSI information, and with information about their [order](https://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Order/#items) with items.


``` 
curl -u $SL_USER:$SL_APIKEY -X GET -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress" 'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/112238162/getObject.json?objectMask=mask%5BbillingItem%5BorderItem%5Border%5Bitems%5D%5D%5D'
```

The same information can be retrieved from the SLCLI as well.


```bash
slcli --format=json call-api Virtual_Guest getObject 
          --id=123456 
          --mask=billingItem.orderItem.order.items
```