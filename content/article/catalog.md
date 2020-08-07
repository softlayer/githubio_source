---
title: "The Catalog"
description: "Details of how to read the product catalog, find prices, item conflicts, location and other restrictions."
date: "2020-08-05"
tags:
    - "article"
    - "sldn"
---

## Packages

The first step in ordering is to find the appropriate [SoftLayer_Product_Package](/reference/services/SoftLayer_Product_Package/) for what you need to order. These packages contain a varierty of items that will describe the order. Each of those items will have properties that define where it  can be ordered, how much it costs, and any restrictions needed to order the item.

[SoftLayer_Product_Package::getAllObject()](/reference/services/SoftLayer_Product_Package/getAllObjects/) is used to get a list of all packages.

```
$ curl -s  -g -u $SL_USER:$SL_APIKEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Package/getAllObjects?objectMask=mask[type[keyName]]'  | python -m json.tool

{
    "id": 0, # Important for using the Product_Package service.
    "isActive": 1, # some packages might be not active, thus not orderable.
    "keyName": "ADDITIONAL_PRODUCTS", # Important for filtering off of.
    "name": "Additional Products",
    "type": {
        "keyName": "ADDITIONAL_SERVICES" # Important for filtering off of.
    }
},
```


While the wider cloud.ibm.com offerings exist in the catalog as packages, they are not usually oderable from the softlayer api. To easily filter these out, the following `objectFilter` can be used

```
curl -s  -g -u $SL_USER:$SL_APIKEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Package/getAllObjects?objectMask=mask[type[keyName]]&objectFilter={"type":{"keyName":{"operation":"!=BLUEMIX_SERVICE"}}}' 
```

### Important Packages

There are several Virtual Server Instance packages, which are all slightly different.

```
$ curl -s  -g -u $SL_USER:$SL_APIKEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Package/getAllObjects?objectMask=mask[id,keyName]&objectFilter={"type":{"keyName":{"operation":"VIRTUAL_SERVER_INSTANCE"}}}' | python -m json.tool
[
    {
# This is the legacy VSI offering. Don't use this one.
        "id": 46,
        "keyName": "CLOUD_SERVER"
    },
    {
# The moderng VSI offering, what you get when ordering from cloud.ibm.com
        "id": 835,
        "keyName": "PUBLIC_CLOUD_SERVER"
    },
    {
# A transient VSI: https://cloud.ibm.com/docs/virtual-servers?topic=virtual-servers-about-vs-transient
        "id": 991,
        "keyName": "TRANSIENT_CLOUD_SERVER"
    },
    {
# A suspended billing VSI. https://cloud.ibm.com/docs/virtual-servers?topic=virtual-servers-requirements
        "id": 1035,
        "keyName": "SUSPEND_CLOUD_SERVER"
    }
]
```

### Platform Pricing

While the SoftLayer Product_Package catalog includes Cloud (previously known as Bluemix) services, the pricing for these is going to be Zero. This is because these are largely placeholder values. These placeholder packages are used as `topLevelBillingItems` on your invoice, and the usage rates are collected once a month when all charges are tallied up.

To find the current pricing for platform services, use the [Global Catalog API](https://cloud.ibm.com/apidocs/resource-catalog/global-catalog).

## Package Presets

Some packages will have presets, which will cover the CPU, RAM, and Boot Disk configurations. Use [SoftLayer_Product_Package::getActivePresets()](/reference/services/SoftLayer_Product_Package/getActivePresets/) to find these configurations.

Notably the `PUBLIC_CLOUD_SERVER` and `BARE_METAL_SERVER` packages require presets to be used when ordering.

## Items

Now that we have found a Package that we are interested in ordering (lets say package id=835, PUBLIC_CLOUD_SERVER for these examples), we need to find their items. For this we will use [SoftLayer_Product_Package::getItems()](/reference/services/SoftLayer_Product_Package/getItems/).


```
curl -s  -g -u $SL_USER:$SL_APIKEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Package/835/getItems' | python -m json.tool

{
    "capacity": "0",  # Important for Ram, CPU, Disk items.
    "description": "Debian GNU/Linux 9.x Stretch /Stable - LAMP Install (64 bit) ",
    "id": 10471,
    "keyName": "OS_DEBIAN_9_X_STRETCH_LAMP_64_BIT",
    "itemCategory": {
        "categoryCode": "os", # Useful for filtering Items.
        "id": 12,
        "name": "Operating System",
    },
    "prices": [
        {
            "hourlyRecurringFee": "0",  # Hourly fee
            "id": 202579, # Needed when actually placing an order
            "locationGroupId": null, # null here means the DEFAULT price.
            "recurringFee": "0", # Monthly fee
        }
    ]
},
```

### Useful Item properties

- [capacityRestrictedProductFlag](https://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item/#capacityrestrictedproductflag) Indicates if this item can only be ordered with certain configurations. Check the Item->prices->[capacityRestrictionType](/reference/datatypes/SoftLayer_Product_Item_Price/#capacityrestrictiontype) to see if this restriction is a Core, Processor, Disk or other type. The item will have a separate price for each orderable capacity level. Generally you will find this on the Storage as a Service offering, and some Operating Systems that charge per core or processor. 
- [conflicts](/reference/datatypes/SoftLayer_Product_Item/#conflicts) will let you know if this item is not orderable with other items in the package. 
- [requirements](/reference/datatypes/SoftLayer_Product_Item/#requirements) will lis any required items if this item is selected


## Price Ids

Each item in a package will have at least one, often several, prices. The "Default" price will be the on with a `locationGroupId` property set to `null`. You can always order wit hthe default price id, and the API will automatically adjust it when ordering in other regions. This can be confirmed with the result of [SoftLayer_Product_Order::verifyOrder()](/reference/services/SoftLayer_Product_Order/verifyOrder/) and [SoftLayer_Product_Order::placeOrder()](/reference/services/SoftLayer_Product_Order/placeOrder/), as their output will have the adjusted priceIds included.

Every item will need a priceId when ordering, even the Zero cost items.

### Capacity Restrictions

Some prices might have a [capacityRestrictionType](/reference/datatypes/SoftLayer_Product_Item_Price/#capacityrestrictiontype) set, in which case that price would only be valid for items that are >= [capacityRestrictionMinimum](/reference/datatypes/SoftLayer_Product_Item_Price/#capacityrestrictionminimum) and <= [capacityRestrictionMaximum](reference/datatypes/SoftLayer_Product_Item_Price/#capacityrestrictionmaximum).

### Locations

Some items may have different prices in certain regions, this is indicated by a special Price object with the `locationGroupId` set to a specific location. You can find the specific datacenters a locationGroup corresponds with by tapping into the item->prices->pricingLocationGroup->locations relationship.


```
curl -s  -g -u $SL_USER:$SL_APIKEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Package/835/getItems?objectMask=mask[prices[pricingLocationGroup[locations]]]' | python -m json.tool 
{
    "capacity": "1000",
    "description": "1 Gbps Private Network Uplink",
    "id": 498,
    "keyName": "1_GBPS_PRIVATE_NETWORK_UPLINK",
    "units": "Mbps",
    "itemCategory": {
        "categoryCode": "port_speed",
    },
    "prices": [
        {
            "hourlyRecurringFee": ".02",
            "id": 899,
            "locationGroupId": null,  # The DEFUALT Price
            "recurringFee": "10",
        },
        {
            "hourlyRecurringFee": ".021",
            "id": 52425,
            "locationGroupId": 503,
            "recurringFee": "10.3",
            "pricingLocationGroup": {
                "description": "Location Group 2",
                "id": 503,
                "locationGroupTypeId": 82,
                "name": "Location Group 2",
                "locations": [
                    {
                        "id": 449610,
                        "name": "mon01"
                    },
                    {
                        "id": 449618,
                        "name": "mon02"
                    },
                    {
                        "id": 448994,
                        "name": "tor01"
                    },
                    {
                        "id": 350993,
                        "name": "tor02"
                    },
                    {
                        "id": 221894,
                        "name": "ams02"
                    },
                    {
                        "id": 265592,
                        "name": "ams01"
                    },
                    {
                        "id": 814994,
                        "name": "ams03"
                    }
                ]
            }
        },
```


## The Order Container

Now that you have collected all the price ids for your order, it is time to put them in a container.

[SoftLayer_Container_Product_Order/](https://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order/) is the generic container, most products will have a special type associated with them. You can specify the specific container with the `complexType` property (even though that isn't really documented...).

For example, a Hardware Server order would have a complexType of `Container_Product_Order_Hardware_Server` and a subnet order would be `Container_Product_Order_Network_Subnet`

The prices go into the `prices` property, as an array of objects. You don't need to specify the Id property of each price. Like this: `"prices": [{"id":1},{"id":100}...]`

If you are ordering multiple products and want to use the same order, you would create a container for each product, and combine them in the [orderContainers](https://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order/#ordercontainers) property of the base container structure.

## Helpful Examples

- [Tagged with Ordering](https://sldn.softlayer.com/tags/order/)
- [Python orderBareMetal](https://sldn.softlayer.com/python/orderBareMetal/)
- [Understanding Ordering](https://sldn.softlayer.com/article/understanding-ordering/)
